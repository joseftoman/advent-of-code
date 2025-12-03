#!/usr/bin/env python

import sys

DIGITS = 12


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
        index = -1
        bank = 0

        for power in range(DIGITS - 1, -1, -1):
            digit, shift = max_with_index(digits[index + 1:len(digits) - power])
            index += shift + 1
            bank += digit * (10 ** power)

        joltage += bank

    print(joltage)


if __name__ == '__main__':
    main()
