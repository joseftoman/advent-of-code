#!/usr/bin/python3

import sys
import re

discs = []
max = None
time = 0

def test_discs(t):
    for d in discs:
        if (d[1] + t) % d[0] != 0: return False
    return True

for line in sys.stdin:
    m_obj = re.match('Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)\.', line);
    size = int(m_obj.group(1))
    discs.append( (size, (int(m_obj.group(2)) + len(discs) + 1) % size) )
    if max is None or max[1] < size: max = ( len(discs) - 1, size )

time = (max[1] - discs[max[0]][1]) % max[1]

while not test_discs(time):
    time += max[1]

print(time)
