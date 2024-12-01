#!/usr/bin/env python

from collections import defaultdict
import sys

similarity = 0
left_counts = defaultdict(int)
right_counts = defaultdict(int)

for line in sys.stdin:
    left_id, right_id = [int(_) for _ in line.split()]
    left_counts[left_id] += 1
    right_counts[right_id] += 1

for left_id, left_count in left_counts.items():
    similarity += left_id * left_count * right_counts.get(left_id, 0)

print(similarity)
