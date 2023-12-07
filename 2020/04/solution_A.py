#!/usr/bin/env python

import sys
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
left = required.copy()
valid = 0


for line in sys.stdin:
    line = line.strip()
    if not line:
        if not left:
            valid += 1
        left = required.copy()
        continue

    for token in line.split():
        field, _ = token.split(':')
        if field != 'cid':
            left.remove(field)

if not left:
    valid += 1

print(valid)
