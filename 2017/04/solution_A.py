#!/usr/bin/python3

import sys
import re

valid = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    words = re.split(r'\s+', line)
    unique = dict.fromkeys(words)
    if len(words) == len(unique.keys()): valid += 1

print(valid)
