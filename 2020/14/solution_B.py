#!/usr/bin/env python

import re
import sys

regex = re.compile(r'mem\[(\d+)\] = (\d+)')


def read_mask(line):
    or_mask = []
    float_mask = []

    _, mask = line.split('=')
    size = len(mask) - 1

    for index, bit in enumerate(reversed(list(mask))):
        if bit == '1':
            or_mask.append(2 ** index)
        elif bit == 'X':
            float_mask.append((2 ** index, 2 ** (size + 1) - 1 - 2 ** index))

    return or_mask, float_mask

def main():
    mem = {}
    or_mask = []
    float_mask = []

    for line in sys.stdin:
        line = line.strip()
        if line[:2] == 'ma':
            or_mask, float_mask = read_mask(line)
            continue

        address, value = [int(_) for _ in regex.fullmatch(line).groups()]

        for mask in or_mask:
            address |= mask

        for bits in range(0, 2 ** len(float_mask)):
            float_address = address

            for index, pair in enumerate(float_mask):
                if bits & (2 ** index):
                    float_address |= pair[0]
                else:
                    float_address &= pair[1]

            mem[float_address] = value

    print(sum(mem.values()))


if __name__ == '__main__':
    main()
