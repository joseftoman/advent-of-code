#!/usr/bin/env python

from collections import defaultdict
import sys

available = defaultdict(set)
options = []
state = 1

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line == 'your ticket:':
        state = 2
        continue
    if line == 'nearby tickets:':
        state = 3
        continue

    if state == 1:
        field, seats = line.split(': ')
        for interval in seats.split(' or '):
            x, y = [int(_) for _ in interval.split('-')]
            for seat in range(x, y + 1):
                available[field].add(seat)
                available['_all'].add(seat)

    if state == 2:
        fields = set(filter(lambda key: key != '_all', available.keys()))
        for seat in [int(_) for _ in line.split(',')]:
            options.append([fields.copy(), seat])

    if state == 3:
        seats = [int(_) for _ in line.split(',')]
        invalid = False
        for seat in seats:
            if seat not in available['_all']:
                invalid = True
                break
        if invalid:
            continue

        for index, seat in enumerate(seats):
            for field in list(options[index][0]):
                if seat not in available[field]:
                    options[index][0].remove(field)

left = set()
done = []
for index, fields in enumerate([_[0] for _ in options]):
    if len(fields) == 1:
        done.append(index)
    else:
        left.add(index)

while left:
    x = done.pop()
    field = list(options[x][0])[0]
    for y in list(left):
        options[y][0].discard(field)
        if len(options[y][0]) == 1:
            done.append(y)
            left.remove(y)

mult = 1
for item in options:
    if list(item[0])[0][:9] == 'departure':
        mult *= item[1]

print(mult)
