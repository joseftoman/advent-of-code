#!/usr/bin/env python

import sys
fuel = 0

for line in sys.stdin:
    fuel += int(int(line) / 3) - 2

print(fuel)
