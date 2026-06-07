#!/usr/bin/env python3
"""Simple Caesar-shift utility.

Usage:
  python isomorphic.py <text> <shift>

If no arguments are provided, a small demo runs.
"""
import sys


def caesar_shift(s: str, k: int) -> str:
    k = k % 26
    out = []
    for ch in s:
        if 'a' <= ch <= 'z':
            base = ord('a')
            out.append(chr((ord(ch) - base - k) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            out.append(chr((ord(ch) - base - k) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)


def main() -> None:
    if len(sys.argv) >= 3:
        text = sys.argv[1]
        try:
            shift = int(sys.argv[2])
        except ValueError:
            print("Error: shift must be an integer", file=sys.stderr)
            sys.exit(2)
        print(caesar_shift(text, shift))
    else:
        # demo
        s = "abc"
        k = 3
        print(caesar_shift(s, k))


if __name__ == '__main__':
    main()