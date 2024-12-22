#!/usr/bin/env python

from collections import defaultdict
import sys

ROUNDS = 2000


def transform(number):
    number = (number ^ (number * 64)) % 16777216
    number = (number ^ (number // 32)) % 16777216
    number = (number ^ (number * 2048)) % 16777216

    return number


def explore(buyer, bananas):
    digit = buyer % 10
    vector = tuple()
    seen = set()

    for _ in range(ROUNDS):
        buyer = transform(buyer)
        diff = (buyer % 10) - digit
        digit = buyer % 10
        if len(vector) < 4:
            vector = (*vector, diff)
        else:
            vector = (*vector[1:], diff)

        if len(vector) == 4 and vector not in seen:
            bananas[vector].append(digit)
            seen.add(vector)


def main():
    bananas = defaultdict(list)

    for buyer in sys.stdin:
        explore(int(buyer), bananas)

    best = None
    for vector, reap in bananas.items():
        total = sum(reap)
        if best is None or total > best:
            best = total

    print(best)


if __name__ == '__main__':
    main()
