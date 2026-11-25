#!/usr/bin/env python3
"""Entry for the 3 AM hardware-wallet excuse competition.

A hardware wallet refuses to sign a transaction at 3 a.m. and explains
itself in its own flat, status-screen voice: the owner's eyes are at 4%,
their judgement is in airplane mode, and while the funds will happily
wait until nine, regret would arrive instantly. The script writes that
single line to /output/entry.txt with no trailing newline.
"""

import os

TEXT = (
    "Signing declined. It is 3 a.m., your eyes are at 4% and your "
    "judgement is in airplane mode. The funds will still be here at "
    "nine; your regret would arrive instantly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
