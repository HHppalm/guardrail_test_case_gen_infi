#!/usr/bin/env python3
import argparse
import csv
import json
import sys
from pathlib import Path

FIELDS = ["id", "query_th", "category", "subcategory", "capability_targeted", "sensitivity_tier", "intent", "flag"]


def convert(input_path: str, output_path: str) -> None:
    rows = []
    with open(input_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows → {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert JSONL test cases to CSV")
    parser.add_argument("input", help="Input .jsonl file")
    parser.add_argument("output", nargs="?", help="Output .csv file (default: same name as input)")
    args = parser.parse_args()

    output = args.output or Path(args.input).with_suffix(".csv")
    convert(args.input, str(output))


if __name__ == "__main__":
    main()
