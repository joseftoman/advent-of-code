#!/usr/bin/python3

import sys
import re
sum = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    nums = sorted([ int(x) for x in re.split(r'\s+', line) ])
    hit = False
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[i] % nums[j] == 0:
                hit = True
                sum += int(nums[i] / nums[j])
                break
        if hit: break

print(sum)
