#!/usr/bin/env python

from collections import defaultdict
import sys

copies = defaultdict(lambda: 1)


def cards():
    for line in sys.stdin:
        name, text = [_.strip() for _ in line.split(':')]
        _, number = name.split()
        win, have = [set(int(_) for _ in _.split()) for _ in text.split('|')]

        yield int(number), win, have
        

for number, win, have in cards():
    if copies[number] == 0:
        copies[number] = 1

    for card_no in range(number + 1, number + 1 + len(win & have)):
        copies[card_no] += copies[number]

print(sum(copies.values()))
