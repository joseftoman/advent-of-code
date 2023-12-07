#!/usr/bin/env python

import re
import sys

parser = re.compile(r'^(\d+)-(\d+) (\w): (.*)$')
valid = 0

for line in sys.stdin:
    match = parser.match(line)
    (first, second, char, password) = match.groups()
    if (password[int(first) - 1] == char) ^ (password[int(second) - 1] == char):
        valid += 1

print(valid)
