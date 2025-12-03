#!/usr/bin/env python

import sys


def max_with_index(digits: list[int]) -> tuple[int, int]:
    best = (None, None)

    for index, digit in enumerate(digits):
        if best[0] is None or digit > best[0]:
            best = (digit, index)

    return best


def main():
    joltage = 0

    for line in sys.stdin:
        digits = [int(_) for _ in line.strip()]
        first, index = max_with_index(digits[:-1])
        second, _ = max_with_index(digits[index + 1:])
        joltage += first * 10 + second

    print(joltage)


if __name__ == '__main__':
    main()
