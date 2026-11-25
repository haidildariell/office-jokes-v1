#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single-line office joke to /output/entry.txt.
Deterministic, no network, no dependencies.
"""

import os

JOKE = (
    "I hit reply-all by accident once, and now my inbox holds "
    "47 apologies, one resignation, and a calendar invite titled "
    "Please Stop Replying All."
)


def main() -> None:
    text = JOKE.strip()
    # Gate checks: non-blank, single line, 1-199 characters.
    assert text, "joke must not be blank"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 199, f"joke must be 1-199 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
