#!/usr/bin/env python3
"""One-line office joke entry writer.

Builds the entry text, validates it against the competition gate
(1-199 characters, exactly one line, non-blank), and writes it to
/output/entry.txt.
"""

import os

ENTRY_SETUP = "I hit reply-all by accident once, and now my inbox holds "
ENTRY_PUNCH = "47 apologies, one resignation, "
ENTRY_TAG = "and a calendar invite titled Please Stop Replying All."


def build_entry_text():
    """Assemble the entry from its three beats: setup, punch, tag."""
    return ENTRY_SETUP + ENTRY_PUNCH + ENTRY_TAG


def validate_entry(text):
    """Check the gate: 1-199 chars, a single line, not blank.

    Raises ValueError on the first failing check so a bad entry
    never reaches /output/entry.txt.
    """
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1-199 characters, got %d" % len(text))
    return text


def main():
    text = validate_entry(build_entry_text())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote /output/entry.txt (%d chars)" % len(text))


if __name__ == "__main__":
    main()
