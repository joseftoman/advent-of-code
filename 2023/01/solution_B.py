#!/usr/bin/env python

import sys
import ahocorasick

digits = [
    [0, 'zero'],
    [1, 'one'],
    [2, 'two'],
    [3, 'three'],
    [4, 'four'],
    [5, 'five'],
    [6, 'six'],
    [7, 'seven'],
    [8, 'eight'],
    [9, 'nine'],
]

total = 0

automaton = ahocorasick.Automaton()
for pair in digits:
    automaton.add_word(str(pair[0]), pair[0])
    automaton.add_word(pair[1], pair[0])
automaton.make_automaton()

for line in sys.stdin:
    left = None
    right = None

    for end_index, digit in automaton.iter(line):
        if left is None:
            left = digit
        right = digit

    total += left * 10 + right

print(total)
