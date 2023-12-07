#!/usr/bin/env python

import string
import sys

polymer = [[None, char] for char in sys.stdin.readline().strip()]
end = len(polymer)
best = end

for to_delete in string.ascii_lowercase:
    reduction = 0
    for item in polymer:
        if to_delete == item[1].lower():
            item[0] = False
            reduction += 1
        else:
            item[0] = True

    left = 0
    while left < end and not polymer[left][0]:
        left += 1
    right = left + 1
    while right < end and not polymer[right][0]:
        right += 1

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

    if end - reduction < best:
        best = end - reduction
    #print(f'{to_delete}: {end - reduction}')

print(best)
