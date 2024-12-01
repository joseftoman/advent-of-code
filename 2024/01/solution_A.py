#!/usr/bin/env python

import sys

distance = 0
left_list = []
right_list = []

for line in sys.stdin:
    left_id, right_id = [int(_) for _ in line.split()]
    left_list.append(left_id)
    right_list.append(right_id)

left_list.sort()
right_list.sort()

for left_id, right_id in zip(left_list, right_list):
    distance += abs(left_id - right_id)

print(distance)
