#!/usr/bin/env python3
"""Fridge Roast: write one roast line to /output/entry.txt."""

import os

ENTRY = "Your ice maker has made three cubes since 2019 \u2014 and it still sends a push notification for each one."

def main():
    # Gate: 1-200 chars, single line, non-blank. Entry is 101 chars.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY.strip() and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")

if __name__ == "__main__":
    main()
