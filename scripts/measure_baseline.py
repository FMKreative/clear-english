#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

from readability import analyse


ROOT = Path(__file__).resolve().parents[1]


def load_cases(path: Path) -> list[dict[str, str]]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure Clear English benchmark outputs.")
    parser.add_argument(
        "--outputs",
        type=Path,
        default=Path("evals/baseline_outputs.json"),
        help="Output snapshot to measure, relative to the project root.",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=None,
        help="Exit with status 1 when the average Flesch score is below this value.",
    )
    args = parser.parse_args()

    source_cases = load_cases(ROOT / "evals/one_pass_cases.json")
    authored_cases = load_cases(ROOT / "evals/user_authored_cases.json")
    outputs = json.loads((ROOT / args.outputs).read_text(encoding="utf-8"))

    rows: list[tuple[str, str, str, float, float]] = []
    for case in source_cases + authored_cases:
        output = outputs[case["id"]]
        metrics = analyse(output)
        rows.append(
            (
                case["id"],
                case.get("input_type", "provided-source"),
                case["domain"],
                metrics["flesch_reading_ease"],
                metrics["average_sentence_length"],
            )
        )

    scores = [row[3] for row in rows]
    average = statistics.mean(scores)

    print("id\tinput_type\tdomain\tflesch\tavg_sentence_words")
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]:.1f}\t{row[4]:.1f}")
    print(f"\ncases={len(rows)}")
    print(f"average_flesch={average:.1f}")
    print(f"median_flesch={statistics.median(scores):.1f}")

    print("\nby_domain")
    by_domain: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        by_domain[row[2]].append(row[3])
    for domain in sorted(by_domain):
        print(
            f"{domain}: cases={len(by_domain[domain])}, "
            f"average_flesch={statistics.mean(by_domain[domain]):.1f}"
        )

    print("by_input_type")
    by_input_type: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        by_input_type[row[1]].append(row[3])
    for input_type in sorted(by_input_type):
        print(
            f"{input_type}: cases={len(by_input_type[input_type])}, "
            f"average_flesch={statistics.mean(by_input_type[input_type]):.1f}"
        )

    if args.fail_under is not None and average < args.fail_under:
        print(
            f"FAIL: average Flesch Reading Ease {average:.1f} is below "
            f"{args.fail_under:.1f}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
