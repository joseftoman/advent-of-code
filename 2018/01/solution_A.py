#!/usr/bin/python

import sys
x = 0

for line in sys.stdin:
    x += int(line)

print(x)
