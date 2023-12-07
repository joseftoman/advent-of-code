#!/usr/bin/env python

import sys

first = [int(_) for _ in sys.stdin.readline().rstrip()]
current = first[0]

cups = {first[i-1]: first[i] for i in range(1, len(first))}
cups[first[-1]] = 10
for i in range(11, 10**6 + 1):
    cups[i - 1] = i
cups[10**6] = first[0]

for _ in range(10**7):
    pick = set()
    pos = current
    for _ in range(3):
        pos = cups[pos]
        pick.add(pos)

    dest = current - 1
    while not dest or dest in pick:
        dest -= 1
        if dest < 1:
            dest = 10**6

    tmp = cups[current]
    cups[current] = cups[pos]
    cups[pos] = cups[dest]
    cups[dest] = tmp

    current = cups[current]

result = cups[1]
result *= cups[result]
print(str(result))
