#!/usr/bin/env python

import re
import sys

regex_cut = re.compile('(-?\d+)')
deck = list(range(10007))

for line in sys.stdin:
    line = line.strip()
    if line == 'deal into new stack':
        deck.reverse()
    elif line[:3] == 'cut':
        cut = int(regex_cut.match(line[4:]).group(1))
        if cut < 0:
            cut = len(deck) + cut
        deck = deck[cut:] + deck[:cut]
    else:
        increment = int(line[20:])
        new_deck = [None] * len(deck)
        for index, item in enumerate(deck):
            new_deck[index * increment % len(deck)] = item
        deck = new_deck

for index, item in enumerate(deck):
    if item == 2019:
        print(index)
        break
