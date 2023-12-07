#!/usr/bin/python

import sys
seen = {0: True}
freqs = []
x = 0

for line in sys.stdin:
    freqs.append(int(line))

while True:
    for f in freqs:
        x += f
        if x in seen:
            print(x)
            sys.exit(0)

        seen[x] = True
