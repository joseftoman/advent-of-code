#!/usr/bin/env python

from collections import defaultdict
import sys

fish = defaultdict(int)
for num in [int(_) for _ in sys.stdin.readline().split(',')]:
    fish[num] += 1

for _ in range(256):
    new_fish = defaultdict(int)

    for state, count in fish.items():
        if state == 0:
            new_fish[6] += count
            new_fish[8] += count
        else:
            new_fish[state-1] += count

    fish = new_fish

total = 0
for count in fish.values():
    total += count

print(total)
