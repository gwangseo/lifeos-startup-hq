"""Small Notion API client for LifeOS data-source exports.

The client intentionally uses only the Python standard library so it can run in
GitHub Actions without dependency installation.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


NOTION_API_BASE = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = "2026-03-11"


DATA_SOURCES = {
    "conversations": {
        "env": "NOTION_CONVERSATION_DATA_SOURCE_ID",
        "csv": "conversations.csv",
    },
    "decision_log": {
        "env": "NOTION_DECISION_DATA_SOURCE_ID",
        "csv": "decision_log.csv",
    },
    "codex_tasks": {
        "env": "NOTION_CODEX_TASK_DATA_SOURCE_ID",
        "csv": "codex_tasks.csv",
    },
    "research_database": {
        "env": "NOTION_RESEARCH_DATA_SOURCE_ID",
        "csv": "research_database.csv",
    },
    "competitors": {
        "env": "NOTION_COMPETITOR_DATA_SOURCE_ID",
        "csv": "competitors.csv",
    },
    "sync_log": {
        "env": "NOTION_SYNC_LOG_DATA_SOURCE_ID",
        "csv": "sync_log.csv",
    },
}


class NotionError(RuntimeError):
    """Raised when the Notion API returns an error."""


@dataclass(frozen=True)
class DataSourceConfig:
    name: str
    env_name: str
    data_source_id: str
    csv_filename: str


def load_dotenv(path: str | Path = ".env") -> None:
    """Load a minimal .env file without overriding existing environment values."""

    env_path = Path(path)
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def configured_data_sources() -> list[DataSourceConfig]:
    configs: list[DataSourceConfig] = []
    for name, details in DATA_SOURCES.items():
        env_name = details["env"]
        data_source_id = os.environ.get(env_name, "").strip()
        if data_source_id:
            configs.append(
                DataSourceConfig(
                    name=name,
                    env_name=env_name,
                    data_source_id=data_source_id,
                    csv_filename=details["csv"],
                )
            )
    return configs


class NotionClient:
    def __init__(
        self,
        token: str | None = None,
        *,
        notion_version: str | None = None,
        max_retries: int = 3,
    ) -> None:
        self.token = token or os.environ.get("NOTION_TOKEN", "")
        self.notion_version = notion_version or os.environ.get(
            "NOTION_VERSION", DEFAULT_NOTION_VERSION
        )
        self.max_retries = max_retries

        if not self.token:
            raise ValueError("NOTION_TOKEN is required.")

    def request(
        self,
        method: str,
        path: str,
        *,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        url = f"{NOTION_API_BASE}{path}"
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
        }

        for attempt in range(self.max_retries + 1):
            request = urllib.request.Request(url, data=body, headers=headers, method=method)
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    response_body = response.read().decode("utf-8")
                    return json.loads(response_body) if response_body else {}
            except urllib.error.HTTPError as exc:
                error_body = exc.read().decode("utf-8")
                retry_after = exc.headers.get("Retry-After")
                if exc.code in {429, 500, 502, 503, 504} and attempt < self.max_retries:
                    wait_seconds = float(retry_after or 2**attempt)
                    time.sleep(wait_seconds)
                    continue
                raise NotionError(f"Notion API {method} {path} failed: {exc.code} {error_body}") from exc
            except urllib.error.URLError as exc:
                if attempt < self.max_retries:
                    time.sleep(2**attempt)
                    continue
                raise NotionError(f"Notion API {method} {path} failed: {exc}") from exc

        raise NotionError(f"Notion API {method} {path} failed after retries.")

    def retrieve_data_source(self, data_source_id: str) -> dict[str, Any]:
        return self.request("GET", f"/data_sources/{data_source_id}")

    def query_data_source(
        self,
        data_source_id: str,
        *,
        start_cursor: str | None = None,
        page_size: int = 100,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {"page_size": page_size}
        if start_cursor:
            payload["start_cursor"] = start_cursor
        return self.request("POST", f"/data_sources/{data_source_id}/query", payload=payload)

    def iter_data_source_pages(self, data_source_id: str) -> Iterable[dict[str, Any]]:
        cursor: str | None = None
        while True:
            response = self.query_data_source(data_source_id, start_cursor=cursor)
            yield from response.get("results", [])
            if not response.get("has_more"):
                break
            cursor = response.get("next_cursor")

