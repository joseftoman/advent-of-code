#!/usr/bin/env python

import sys


def halfs(num: str) -> tuple[int, int]:
    left = num[:len(num) // 2]
    right = num[len(num) // 2:]

    return int(left), int(right)


def main():
    output = 0

    for interval in next(sys.stdin).strip().split(','):
        start, end = interval.split('-', maxsplit=1)

        if len(start) % 2:
            minimum = 10 ** (len(start) // 2)
        else:
            left, right = halfs(start)
            minimum = left if left >= right else left + 1

        if len(end) % 2:
            maximum = 10 ** (len(start) // 2) - 1
        else:
            left, right = halfs(end)
            maximum = left if left <= right else left - 1

        for item in range(minimum, maximum + 1):
            output += int(f'{item}{item}')

    print(output)

if __name__ == '__main__':
    main()
