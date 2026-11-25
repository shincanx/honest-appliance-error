#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun bounty entry.

Writes exactly one line (<=200 chars, UTF-8) to $MAKEFUN_OUTPUT_DIR/entry.txt
and prints it. Fully deterministic, exit 0.
"""
import os
import sys

LINE = (
    "ERROR E04: Unbalanced load detected. "
    "I will now walk across the kitchen. Please remove one sock."
)


def main() -> int:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "no leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
