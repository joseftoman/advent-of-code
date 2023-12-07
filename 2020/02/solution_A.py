#!/usr/bin/env python

import re
import sys

parser = re.compile(r'^(\d+)-(\d+) (\w): (.*)$')
valid = 0

for line in sys.stdin:
    match = parser.match(line)
    (low, high, char, password) = match.groups()
    if int(low) <= len([_ for _ in password if _ == char]) <= int(high):
        valid += 1

print(valid)
