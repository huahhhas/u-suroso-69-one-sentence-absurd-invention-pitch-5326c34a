#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun bounty entry.

Writes exactly one sentence pitching an absurd invention to
/output/entry.txt (no trailing newline).
"""

import hashlib
import os
import re

LINE = (
    "The Self-Watering Fern That Waters You Back: a fern with a tiny pump "
    "that mists its owner every morning, so the plant stays alive and you "
    "finally drink enough water."
)
# Why this line fits the brief: an absurd invention (a houseplant that
# waters its owner instead of the other way round) with a concrete
# mechanism (a tiny pump misting the owner each morning) and a human
# payoff (the plant survives and the owner finally drinks enough water)
# — funny, specific, and easy to picture in a single sentence.

OUTPUT = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(OUTPUT, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 220, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not equal the expected line"
    # No trailing newline: the file must be exactly the 165 characters.
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert len(raw) == len(text) == 165, "entry must be exactly 165 bytes"
    # Exactly one sentence: one terminal period, at the end.
    assert text.count(".") == 1 and text.endswith("."), "not exactly one sentence"
    assert re.search(r"[.!?]", text) is not None
    print("sha256:", hashlib.sha256(raw).hexdigest())
    print("chars:", len(text))


if __name__ == "__main__":
    main()
