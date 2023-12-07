#!/usr/bin/env python

import sys

points = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6,
}

score = 0

for line in sys.stdin:
    game = tuple(line.strip().split())
    score += points[game]

print(score)
