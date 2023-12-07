#!/usr/bin/env python

from functools import cmp_to_key
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
    packets = [[[2]], [[6]]]
    decoder_key = 1

    while True:
        pair = [json.loads(sys.stdin.readline().strip()) for _ in range(2)]
        packets.extend(pair)
        blank = sys.stdin.readline()
        if not blank:
            break

    packets.sort(key=cmp_to_key(compare))
    for index, packet in enumerate(packets, 1):
        if packet == [[2]] or packet == [[6]]:
            decoder_key *= index

    print(decoder_key)


if __name__ == '__main__':
    main()
