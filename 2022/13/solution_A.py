#!/usr/bin/env python

import json
import sys


def cmp_int(left, right) -> int:
    return (left > right) - (left < right)


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return cmp_int(left, right)

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for index in range(min(len(left), len(right))):
        inner = compare(left[index], right[index])
        if inner:
            return inner

    return cmp_int(len(left), len(right))


def main():
    correct = 0
    index = 0

    while True:
        pair = [json.loads(sys.stdin.readline().strip()) for _ in range(2)]
        index += 1
        if compare(*pair) == -1:
            correct += index
        blank = sys.stdin.readline()
        if not blank:
            break

    print(correct)


if __name__ == '__main__':
    main()
