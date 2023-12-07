#!/usr/bin/env python

from collections import deque
import re
import sys

def score(d):
    mult = 1
    total = 0

    while d:
        total += d.pop() * mult
        mult += 1

    return total

one = deque()
two = deque()

sys.stdin.readline()
for line in sys.stdin:
    if not line.strip():
        break
    one.append(int(line))

sys.stdin.readline()
for line in sys.stdin:
    two.append(int(line))

while one and two:
    c1 = one.popleft()
    c2 = two.popleft()
    if c1 > c2:
        one.extend([c1, c2])
    else:
        two.extend([c2, c1])

print(score(one) if one else score(two))
