#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes one original roast line about a smart fridge to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
Python 3 standard library only. Deterministic: the same line
every run, byte for byte.
"""

import os
import sys

# Original line, written for this entry: the fridge's firmware update
# turns it into a smug little manager that grades your midnight snacks.
LINE = (
    "My smart fridge updated its firmware at midnight and now it greets "
    "me every morning with a push notification ranking my midnight snacks."
)


def validate(line: str) -> str:
    """Check the entry line before writing: non-empty, one line, <= 200 chars."""
    assert line, "entry line must not be empty"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= 200, f"entry too long: {len(line)} characters (limit 200)"
    return line


def main() -> int:
    line = validate(LINE.strip())
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
