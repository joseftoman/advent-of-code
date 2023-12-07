#!/usr/bin/env python

import sys

full_cover = 0

for line in sys.stdin:
    left, right = line.strip().split(',')
    left = [int(_) for _ in left.split('-')]
    right = [int(_) for _ in right.split('-')]
    if len(set(range(left[0], left[1] + 1)) | set(range(right[0], right[1] + 1))) == max(left[1] - left[0] + 1, right[1] - right[0] + 1):
        full_cover += 1

print(full_cover)
