#!/usr/bin/env python3
"""
export_raw: render each idea in data/ideas.json as a raw source document.

Output goes to raw/business-ideas/<slug>.md, one file per idea, formatted
for the llm-wiki pattern (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
immutable, curated source material that an ingest skill reads once and
folds into wiki pages. No wikilinks or synthesis here, only frontmatter
plus the underlying facts - that stays the ingest step's job.

USAGE
    python3 cli/export_raw.py [--out DIR] [--retrieved-at YYYY-MM-DD]

Regenerate whenever data/ideas.json changes; treat raw/business-ideas/
as a build artifact, not something to hand-edit.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = REPO_ROOT / "data" / "ideas.json"
DEFAULT_OUT = REPO_ROOT / "raw" / "business-ideas"


def yaml_str(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(yaml_str(v) for v in values) + "]"


def frontmatter(idea: dict[str, Any], retrieved_at: str) -> str:
    lines = [
        "---",
        "type: source",
        "source: businessideasdb.com",
        "dataset: business-ideas-dataset",
        f"dataset_id: {idea['id']}",
        f"slug: {idea['slug']}",
        f"title: {yaml_str(idea['title'])}",
        f"url: {idea['url']}",
        f"retrieved_at: {retrieved_at}",
        f"category: {yaml_str(idea['category'])}",
        f"tags: {yaml_list(idea.get('tags') or [])}",
        f"opportunity_score: {idea['opportunity_score']}",
        f"problem_score: {idea['problem_score']}",
        f"feasibility_score: {idea['feasibility_score']}",
        f"timing_score: {idea['timing_score']}",
        f"competition: {yaml_str(idea['competition'])}",
        f"difficulty: {yaml_str(idea['difficulty'])}",
        f"revenue_range: {yaml_str(idea['revenue_range'])}",
        f"search_volume: {idea['search_volume']}",
        f"growth_percent: {idea['growth_percent']}",
        f"competitors: {yaml_list(idea.get('competitor_names') or [])}",
        f"dataset_created_at: {yaml_str(idea['created_at'])}",
        f"dataset_updated_at: {yaml_str(idea['updated_at'])}",
        "---",
    ]
    return "\n".join(lines)


def body(idea: dict[str, Any]) -> str:
    tags = ", ".join(idea.get("tags") or []) or "-"
    competitors = idea.get("competitor_names") or []
    competitors_md = "\n".join(f"- {c}" for c in competitors) if competitors else "- (none named)"
    growth = idea.get("growth_percent")
    growth_str = f"{growth:+d}%" if growth is not None else "-"
    signal_count = idea.get("signal_count")
    signal_count_str = str(signal_count) if signal_count is not None else "-"

    return f"""# {idea['title']}

> {idea['pitch']}

## Market signal

- Keyword: `{idea['keyword']}`
- US monthly search volume: {idea['search_volume']} (YoY growth: {growth_str})
- Competition: {idea['competition']}
- Estimated revenue range: {idea['revenue_range']}
- Supporting signal count: {signal_count_str}

## AI scores (0-10, BID rubric)

- Opportunity: {idea['opportunity_score']}
- Problem severity: {idea['problem_score']}
- Feasibility: {idea['feasibility_score']}
- Timing: {idea['timing_score']}

## Build

- Category: {idea['category']}
- Difficulty: {idea['difficulty']}
- Tags: {tags}

## Named competitors

{competitors_md}

## Source

Full editorial analysis (customer profile, MVP feature list, Reddit thread URLs,
competitor research) lives at: {idea['url']}

Dataset entry created {idea['created_at']}, last updated {idea['updated_at']}.
"""


def render(idea: dict[str, Any], retrieved_at: str) -> str:
    return frontmatter(idea, retrieved_at) + "\n\n" + body(idea)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output directory (default: raw/business-ideas)")
    p.add_argument(
        "--retrieved-at",
        default=date.today().isoformat(),
        help="Value stamped on retrieved_at frontmatter (default: today, UTC)",
    )
    args = p.parse_args()

    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(DATASET_PATH.read_text())
    ideas = data["ideas"]

    args.out.mkdir(parents=True, exist_ok=True)
    for idea in ideas:
        out_path = args.out / f"{idea['slug']}.md"
        out_path.write_text(render(idea, args.retrieved_at))

    print(f"Wrote {len(ideas)} raw source files to {args.out}")


if __name__ == "__main__":
    main()
