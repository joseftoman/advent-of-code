#!/usr/bin/env python

import sys
two = 0
three = 0

for line in sys.stdin:
    chars = {}
    has_two = False
    has_three = False

    for char in line.strip():
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    for char, count in chars.items():
        if count == 2:
            has_two = True
        if count == 3:
            has_three = True

    if has_two:
        two += 1
    if has_three:
        three += 1

print(two * three)
