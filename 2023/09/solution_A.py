#!/usr/bin/env python

import sys


def get_next(seq):
    if all(_ == 0 for _ in seq):
        return 0

    next_diff = get_next([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])
    return seq[-1] + next_diff


def main():
    total = 0
    for line in sys.stdin:
        history = [int(_) for _ in line.strip().split()]
        total += get_next(history)

    print(total)


if __name__ == '__main__':
    main()
