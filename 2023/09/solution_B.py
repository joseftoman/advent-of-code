#!/usr/bin/env python

import sys


def get_prev(seq):
    if all(_ == 0 for _ in seq):
        return 0

    prev_diff = get_prev([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])
    return seq[0] - prev_diff


def main():
    total = 0
    for line in sys.stdin:
        history = [int(_) for _ in line.strip().split()]
        total += get_prev(history)

    print(total)


if __name__ == '__main__':
    main()
