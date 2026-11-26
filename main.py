#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Writes one original fortune-cookie line for software developers to
``entry.txt`` in the output directory.
"""

import os
import sys

FORTUNE = "Your greatest legacy will be a function nobody dares to delete, including you."


def output_dir():
    """Grader output first, then /output, then this program's folder."""
    candidates = [
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            os.makedirs(candidate, exist_ok=True)
        except OSError:
            continue
        if os.access(candidate, os.W_OK):
            return candidate
    return os.path.dirname(os.path.abspath(__file__))


def main():
    line = FORTUNE.strip()
    if not 1 <= len(line) <= 120:
        print(
            "fortune line must be 1-120 characters, got %d" % len(line),
            file=sys.stderr,
        )
        return 1
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read back what was written: the file must hold exactly this line.
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != line + "\n":
        print("entry.txt does not match the fortune line", file=sys.stderr)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
