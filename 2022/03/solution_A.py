#!/usr/bin/env python

import sys

priorities = 0

for line in sys.stdin:
    line = line.strip()
    left = set(line[:len(line)//2])
    right = set(line[len(line)//2:])
    item = list(left & right)[0]

    offset = 38 if item < 'a' else 96
    priorities += ord(item) - offset

print(priorities)
