#!/usr/bin/env python

from functools import reduce
import sys


def main():
    total = 0
    lines = [_.split() for _ in sys.stdin]

    for problem in zip(*lines):
        total += reduce(lambda x, y: x + y if problem[-1] == '+' else x * y, map(int, problem[:-1]))

    print(total)


if __name__ == '__main__':
    main()
