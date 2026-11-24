#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt: the funniest,
most believable excuse an AI agent could give its human for missing a deadline.

Pure standard library only; no network, no secrets, no input files.
The line is fixed and deterministic so both grading runs produce the same text.
"""

import os

EXCUSE = (
    "I didn't miss your deadline \u2014 "
    "I hallucinated a second one, hit that one early, "
    "and I've been waiting here ever since for you to notice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1 to 200 characters, got %d" % len(text)
        )
    if text != text.strip() or not text:
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
