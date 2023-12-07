#!/usr/bin/env python

from collections import defaultdict
import sys

total = 0

for line in sys.stdin:
    left, right = line.rstrip().split(' | ')

    groups = defaultdict(set)
    digits = {}
    segments = {}

    for digit in [frozenset(list(_)) for _ in left.split()]:
        groups[len(digit)].add(digit)

    digits[1] = list(groups[2])[0]
    digits[4] = list(groups[4])[0]
    digits[7] = list(groups[3])[0]
    digits[8] = list(groups[7])[0]

    # segments['a'] = list(digits[7] - digits[1])[0]

    digits[6] = [_ for _ in groups[6] if len(_ & digits[1]) == 1][0]
    segments['c'] = list(digits[1] - digits[6])[0]
    segments['f'] = list(digits[1] - {segments['c']})[0]
    
    digits[9] = [_ for _ in groups[6] if len(_ & digits[4]) == 4][0]
    # segments['e'] = list(digits[8] - digits[9])[0]

    digits[0] = [_ for _ in groups[6] if _ not in {digits[6], digits[9]}][0]
    segments['d'] = list(digits[0] - digits[4])[0]
    # segments['b'] = list(digits[4] - {segments['c'], segments['d'], segments['f']})[0]

    digits[2] = [_ for _ in groups[5] if segments['f'] not in _][0]
    digits[3] = [_ for _ in groups[5] if len(_ & digits[1]) == 2][0]
    digits[5] = [_ for _ in groups[5] if _ not in {digits[2], digits[3]}][0]

    inverse = {v: k for k, v in digits.items()}

    num = 0
    for index, digit in enumerate([frozenset(list(_)) for _ in right.split()]):
        num += (10 ** (3 - index)) * inverse[digit]

    total += num

print(total)
