#!/usr/bin/env python

import sys


def main():
    total = 0
    for step in [_ for _ in next(sys.stdin).strip().split(',')]:
        value = 0
        for char in step:
            value = ((value + ord(char)) * 17) % 256
        total += value

    print(total)


if __name__ == '__main__':
    main()
