#!/usr/bin/env python

from collections import defaultdict
import sys


def do_blink(stone):
    if stone == 0:
        return [1]

    if len(label := str(stone)) % 2 == 0:
        return [int(label[:len(label) // 2]), int(label[len(label) // 2:])]

    return [stone * 2024]


def main():
    target = 75

    stones = defaultdict(int)
    for stone in [int(_) for _ in next(sys.stdin).split()]:
        stones[stone] += 1

    for step in range(target):
        after_blink = defaultdict(int)

        for stone, amount in stones.items():
            for next_stone in do_blink(stone):
                after_blink[next_stone] += amount

        stones = after_blink

    print(sum(stones.values()))


if __name__ == '__main__':
    main()
