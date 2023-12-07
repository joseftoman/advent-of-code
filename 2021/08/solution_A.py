#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    left, right = line.rstrip().split(' | ')
    count += len([_ for _ in right.split() if len(_) in {2, 3, 4, 7}])

print(count)
