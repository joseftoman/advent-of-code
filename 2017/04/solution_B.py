#!/usr/bin/python3

import sys
import re
from collections import Counter

valid = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    words = re.split(r'\s+', line)
    words2 = []

    for w in words:
        w2 = ''
        chars = Counter(w)
        for ch in sorted(chars.keys()):
            w2 += ch+str(chars[ch])

        words2.append(w2)

    unique = dict.fromkeys(words2)
    if len(words2) == len(unique.keys()): valid += 1

print(valid)
