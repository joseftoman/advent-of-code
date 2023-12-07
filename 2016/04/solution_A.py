#!/usr/bin/python3

import sys
import re

sum = 0

for line in sys.stdin:
    m_obj = re.match('(.*)-(\d+)\[(.*)]$', line)
    counts = {}

    for ch in m_obj.group(1):
        if ch == '-': continue
        if ch not in counts: counts[ch] = 0
        counts[ch] += 1

    key_func = lambda ch: 1000 * counts[ch] + 200 - ord(ch)
    sign = ''.join(sorted(counts.keys(), key = key_func, reverse = True)[:5])
    if sign == m_obj.group(3): sum += int(m_obj.group(2))

print(sum)
