#!/usr/bin/python3

import sys
score = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    pos = 0
    nesting = 0
    garbage = False

    while pos < len(line):
        if line[pos] == '>':
            garbage = False
        elif garbage:
            if line[pos] == '!':
                pos += 1
        elif line[pos] == '<':
            garbage = True
        elif line[pos] == '{':
            nesting += 1
        elif line[pos] == '}':
            score += nesting
            nesting -= 1

        pos += 1

print(score)
