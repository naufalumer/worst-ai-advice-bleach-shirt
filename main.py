"""Worst AI Advice entry: write one line of terrible AI advice to /output/entry.txt.

Fully deterministic: the line is hardcoded, no randomness, no clock, no network.
Run outside the grader container with MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The line is a literal on purpose: the grader runs the program twice and
# both runs must write the same bytes, and the judge reads exactly the
# bytes in entry.txt, so nothing here may vary (no randomness, no clock).
LINE = (
    "Certainly! To remove a stain, bleach the entire shirt \u2014 "
    "if everything is white, nothing stands out."
)


# Gate: the sealed scorer accepts 1 to 140 characters. Fail loudly here
# rather than shipping an invalid entry if the line is ever edited.
MAX_CHARS = 140


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
