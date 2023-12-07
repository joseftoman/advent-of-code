#!/usr/bin/python3

import sys
import re

def decrypt(ch, id):
    if ch == '-': return ' '
    return chr((ord(ch) - 97 + id) % 26 + 97)

for line in sys.stdin:
    m_obj = re.match('(.*)-(\d+)\[(.*)]$', line)
    counts = {}

    for ch in m_obj.group(1):
        if ch == '-': continue
        if ch not in counts: counts[ch] = 0
        counts[ch] += 1

    key_func = lambda ch: 1000 * counts[ch] + 200 - ord(ch)
    sign = ''.join(sorted(counts.keys(), key = key_func, reverse = True)[:5])
    if sign != m_obj.group(3): continue

    
    room_name = ''.join([ decrypt(ch, int(m_obj.group(2))) for ch in m_obj.group(1) ])
    if room_name == 'northpole object storage': print(m_obj.group(2))
