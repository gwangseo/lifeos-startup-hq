"""Export LifeOS Notion data sources to CSV files under data/."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

from notion_client import (
    DataSourceConfig,
    NotionClient,
    configured_data_sources,
    load_dotenv,
)


METADATA_COLUMNS = [
    "notion_page_id",
    "notion_url",
    "created_time",
    "last_edited_time",
    "archived",
    "in_trash",
]


def rich_text_to_plain_text(items: list[dict[str, Any]]) -> str:
    return "".join(item.get("plain_text", "") for item in items or [])


def date_to_text(value: dict[str, Any] | None) -> str:
    if not value:
        return ""
    start = value.get("start", "")
    end = value.get("end")
    return f"{start} -> {end}" if end else start


def user_to_text(user: dict[str, Any]) -> str:
    return user.get("name") or user.get("id", "")


def file_to_text(file_value: dict[str, Any]) -> str:
    if file_value.get("type") == "external":
        return file_value.get("external", {}).get("url", "")
    if file_value.get("type") == "file":
        return file_value.get("file", {}).get("url", "")
    return file_value.get("name", "")


def rollup_to_text(rollup: dict[str, Any]) -> str:
    rollup_type = rollup.get("type")
    if rollup_type == "array":
        return "; ".join(property_to_text(item) for item in rollup.get("array", []))
    if rollup_type:
        return property_to_text({"type": rollup_type, rollup_type: rollup.get(rollup_type)})
    return json.dumps(rollup, ensure_ascii=False, sort_keys=True)


def formula_to_text(formula: dict[str, Any]) -> str:
    formula_type = formula.get("type")
    if not formula_type:
        return ""
    return property_to_text({"type": formula_type, formula_type: formula.get(formula_type)})


def property_to_text(prop: dict[str, Any]) -> str:
    prop_type = prop.get("type")
    value = prop.get(prop_type) if prop_type else None

    if value is None:
        return ""
    if prop_type == "title":
        return rich_text_to_plain_text(value)
    if prop_type == "rich_text":
        return rich_text_to_plain_text(value)
    if prop_type == "number":
        return str(value)
    if prop_type in {"select", "status"}:
        return value.get("name", "")
    if prop_type == "multi_select":
        return "; ".join(item.get("name", "") for item in value)
    if prop_type == "date":
        return date_to_text(value)
    if prop_type == "checkbox":
        return "true" if value else "false"
    if prop_type in {"url", "email", "phone_number", "created_time", "last_edited_time"}:
        return str(value)
    if prop_type == "people":
        return "; ".join(user_to_text(user) for user in value)
    if prop_type in {"created_by", "last_edited_by"}:
        return user_to_text(value)
    if prop_type == "files":
        return "; ".join(file_to_text(item) for item in value)
    if prop_type == "relation":
        return "; ".join(item.get("id", "") for item in value)
    if prop_type == "rollup":
        return rollup_to_text(value)
    if prop_type == "formula":
        return formula_to_text(value)
    if prop_type == "unique_id":
        prefix = value.get("prefix")
        number = value.get("number")
        return f"{prefix}-{number}" if prefix else str(number or "")

    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def schema_property_names(schema: dict[str, Any]) -> list[str]:
    properties = schema.get("properties", {})
    return list(properties.keys())


def row_from_page(page: dict[str, Any], property_names: list[str]) -> dict[str, str]:
    properties = page.get("properties", {})
    row = {
        "notion_page_id": page.get("id", ""),
        "notion_url": page.get("url", ""),
        "created_time": page.get("created_time", ""),
        "last_edited_time": page.get("last_edited_time", ""),
        "archived": str(page.get("archived", "")),
        "in_trash": str(page.get("in_trash", "")),
    }
    for name in property_names:
        row[name] = property_to_text(properties.get(name, {}))
    return row


def export_data_source(
    client: NotionClient,
    config: DataSourceConfig,
    *,
    data_dir: Path,
) -> int:
    schema = client.retrieve_data_source(config.data_source_id)
    property_names = schema_property_names(schema)
    rows = [
        row_from_page(page, property_names)
        for page in client.iter_data_source_pages(config.data_source_id)
    ]

    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / config.csv_filename
    headers = METADATA_COLUMNS + property_names

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows):>4} rows -> {output_path}")
    return len(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default="data", help="Directory for CSV exports.")
    parser.add_argument(
        "--only",
        choices=["all", *[config.name for config in configured_data_sources()]],
        default="all",
        help="Optionally export one configured data source.",
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv()
    args = parse_args()

    configs = configured_data_sources()
    if args.only != "all":
        configs = [config for config in configs if config.name == args.only]

    if not configs:
        print("No Notion data sources are configured. Check your environment variables.", file=sys.stderr)
        return 1

    client = NotionClient()
    data_dir = Path(args.data_dir)

    failures: list[str] = []
    total_rows = 0
    for config in configs:
        try:
            total_rows += export_data_source(client, config, data_dir=data_dir)
        except Exception as exc:  # noqa: BLE001 - fail after reporting all attempted exports.
            failures.append(f"{config.name}: {exc}")
            print(f"Failed {config.name}: {exc}", file=sys.stderr)

    print(f"Total rows exported: {total_rows}")

    if failures:
        print("One or more exports failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
