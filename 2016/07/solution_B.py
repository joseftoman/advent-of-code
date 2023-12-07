#!/usr/bin/python3

import sys
import re

ok = 0

for line in sys.stdin:
    line = line.rstrip()
    first = None
    second = None
    skip = False
    aba = set()

    for ch in line:
        if ch == '[': skip = True
        if ch == ']': skip = False

        if first is None:
            first = ch
        elif second is None:
            second = ch
        else:
            if not skip and first == ch and second != first and first.isalpha() and second.isalpha():
                aba.add(first + second + ch)
            first = second
            second = ch

    for seg in aba:
        regex = r'[[^[\]]*'+seg[1]+seg[0]+seg[1]+r'[^[\]]*]'
        if re.search(regex, line):
            ok += 1
            break

print(ok)
