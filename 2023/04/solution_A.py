#!/usr/bin/env python

import sys

points = 0


def cards():
    for line in sys.stdin:
        _, text = [_.strip() for _ in line.split(':')]
        win, have = [set(int(_) for _ in _.split()) for _ in text.split('|')]
        yield win, have
        

for win, have in cards():
    if (match := len(win & have)):
        points += 2 ** (match - 1)

print(points)
