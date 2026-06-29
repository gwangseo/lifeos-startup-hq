"""Scaffold for exporting selected Notion CSV rows into Markdown files.

This first version is intentionally conservative: it reads the CSV exports and
creates Markdown files only for rows that can be safely routed by source type.
Extend ROUTES as Notion properties become final.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Iterable


ROUTES = {
    "decision_log.csv": Path("docs/operations/decisions"),
    "competitors.csv": Path("research/competitors"),
    "research_database.csv": Path("research/sources"),
    "codex_tasks.csv": Path("docs/automation/codex-tasks"),
}


TITLE_CANDIDATES = [
    "Name",
    "Title",
    "Topic",
    "Decision",
    "Task",
    "Run",
]


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or fallback


def first_present(row: dict[str, str], keys: Iterable[str]) -> str:
    for key in keys:
        value = row.get(key, "").strip()
        if value:
            return value
    return ""


def row_to_markdown(row: dict[str, str], title: str) -> str:
    lines = [f"# {title}", ""]
    for key, value in row.items():
        if value:
            lines.extend([f"## {key}", "", value, ""])
    return "\n".join(lines).rstrip() + "\n"


def export_csv(csv_path: Path, output_root: Path, *, dry_run: bool) -> int:
    route = ROUTES.get(csv_path.name)
    if not route:
        return 0

    output_dir = output_root / route
    exported = 0

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = first_present(row, TITLE_CANDIDATES)
            if not title:
                continue

            page_id = row.get("notion_page_id", "").replace("-", "")
            fallback = page_id[:12] or "notion-row"
            output_path = output_dir / f"{slugify(title, fallback)}.md"

            exported += 1
            if dry_run:
                print(f"Would export {csv_path.name}: {title} -> {output_path}")
                continue

            output_dir.mkdir(parents=True, exist_ok=True)
            output_path.write_text(row_to_markdown(row, title), encoding="utf-8")
            print(f"Exported {output_path}")

    return exported


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default="data", help="Directory containing CSV exports.")
    parser.add_argument("--output-root", default=".", help="Repository root for Markdown outputs.")
    parser.add_argument("--dry-run", action="store_true", help="Preview Markdown exports.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data_dir = Path(args.data_dir)
    output_root = Path(args.output_root)

    total = 0
    for csv_path in sorted(data_dir.glob("*.csv")):
        total += export_csv(csv_path, output_root, dry_run=args.dry_run)

    print(f"Markdown rows processed: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

