#!/usr/bin/env python3
"""The Moon Finally Answers Back — a single line spoken back by the Moon."""

import os

LINE = "I kept every promise you made at 2 a.m. \u2014 want me to read them back out loud?"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
