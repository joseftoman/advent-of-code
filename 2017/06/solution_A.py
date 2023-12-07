#!/usr/bin/python3

import sys
import re

banks = [ int(x) for x in re.split(r'\s+', sys.stdin.readline().rstrip()) ]
size = len(banks)
steps = 0
known = {}

def add_state(s):
    s = '.'.join([ str(n) for n in s ])
    if s in known:
        print(steps)
        exit()
    else:
        known[s] = 1

add_state(banks)

while True:
    top = [ None, -1 ]
    for i in range(0, size):
        if banks[i] > top[1]: top = [ i, banks[i] ]

    banks[top[0]] = 0
    x = top[1] // size
    mod = top[1] % size
    pos = (top[0] + 1) % size

    for i in range(0, size):
        banks[pos] += x
        if mod > 0:
            banks[pos] += 1
            mod -= 1
        pos = (pos + 1) % size

    steps += 1
    add_state(banks)
