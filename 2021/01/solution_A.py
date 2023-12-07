#!/usr/bin/env python

import sys

prev = None
inc = 0

for num in [int(_) for _ in sys.stdin]:
    if prev is not None and prev < num:
        inc += 1
    prev = num

print(inc)
