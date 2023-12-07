#!/usr/bin/env python

import sys

report = [_.strip() for _ in sys.stdin]
size = len(report[0])
report = [int(f'0b{_}', 2) for _ in report]

oxy = set(report)
co2 = set(report)

index = size
while len(oxy) > 1:
    index -= 1
    sets = {0: set(), 1: set()}

    for num in oxy:
        if num & (2 ** index):
            sets[1].add(num)
        else:
            sets[0].add(num)

    if len(sets[0]) > len(sets[1]):
        oxy = sets[0]
    else:
        oxy = sets[1]


index = size
while len(co2) > 1:
    index -= 1
    sets = {0: set(), 1: set()}

    for num in co2:
        if num & (2 ** index):
            sets[1].add(num)
        else:
            sets[0].add(num)

    if len(sets[1]) < len(sets[0]):
        co2 = sets[1]
    else:
        co2 = sets[0]

print(oxy.pop() * co2.pop())
