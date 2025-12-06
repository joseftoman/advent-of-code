#!/usr/bin/env python

from functools import reduce
import sys


def main():
    total = 0
    lines = [_.strip('\n') for _ in sys.stdin]

    pos = len(lines[0]) - 1
    buffer = []

    while pos >= 0:
        digits = [int(lines[row][pos]) for row in range(0, len(lines) - 1) if lines[row][pos] != ' ']
        num = 0
    
        for power, digit in enumerate(reversed(digits)):
            num += digit * 10 ** power

        buffer.append(num)

        op = lines[-1][pos]
        pos -= 1

        if op != ' ':
            total += reduce(lambda x, y: x + y if op == '+' else x * y, buffer)
            buffer = []
            pos -= 1

    print(total)


if __name__ == '__main__':
    main()
