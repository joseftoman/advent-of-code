#!/usr/bin/env python

import re
import sys

regex = re.compile(r'mem\[(\d+)\] = (\d+)')


def read_mask(line):
    or_mask = []
    and_mask = []

    _, mask = line.split('=')
    size = len(mask) - 1

    for index, bit in enumerate(reversed(list(mask))):
        if bit == '1':
            or_mask.append(2 ** index)
        elif bit == '0':
            and_mask.append(2 ** (size + 1) - 1 - 2 ** index)

    return or_mask, and_mask


def main():
    mem = {}
    or_mask = []
    and_mask = []

    for line in sys.stdin:
        line = line.strip()
        if line[:2] == 'ma':
            or_mask, and_mask = read_mask(line)
            continue

        address, value = [int(_) for _ in regex.fullmatch(line).groups()]
        for mask in or_mask:
            value |= mask
        for mask in and_mask:
            value &= mask
        mem[address] = value

    print(sum(mem.values()))

if __name__ == '__main__':
    main()
