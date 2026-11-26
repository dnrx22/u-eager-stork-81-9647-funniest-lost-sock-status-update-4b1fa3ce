#!/usr/bin/env python3
"""Write one status update from a lost sock to entry.txt.

Deterministic: the same line is written on every run.
Standard library only, no network access.
"""

import os
import sys

LINE = "Day 12 behind the dryer. The lint here has formed a union. I have been denied exit."

MAX_CHARS = 120


def validate(line: str) -> None:
    if not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
