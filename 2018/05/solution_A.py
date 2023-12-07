#!/usr/bin/env python

import sys
import re

polymer = [[True, char] for char in sys.stdin.readline().strip()]
left = 0
right = 1
end = len(polymer)
reduction = 0

while right < end:
    if polymer[left][1] != polymer[right][1] and polymer[left][1].lower() == polymer[right][1].lower():
        #print(f'{left}, {right}: {polymer[left][1]}{polymer[right][1]}')
        reduction += 2
        polymer[left][0] = False
        polymer[right][0] = False

        left -= 1
        while left >= 0 and not polymer[left][0]:
            left -= 1
        if left < 0:
            left = right + 1
    else:
        left += 1

    while left < end and not polymer[left][0]:
        left += 1

    right = left + 1
    while right < end and not polymer[right][0]:
        right += 1

print(end - reduction)
