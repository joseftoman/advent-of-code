#!/usr/bin/python3

import sys
import re
sum = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    nums = [ int(x) for x in re.split(r'\s+', line) ]
    sum += max(nums) - min(nums)

print(sum)
