#!/usr/bin/env python

import sys

ROUNDS = 2000


def transform(number, rounds):
    for _ in range(rounds):
        number = (number ^ (number * 64)) % 16777216
        number = (number ^ (number // 32)) % 16777216
        number = (number ^ (number * 2048)) % 16777216

    return number


def main():
    print(sum(transform(int(_), ROUNDS) for _ in sys.stdin))


if __name__ == '__main__':
    main()
