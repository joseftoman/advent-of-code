#!/usr/bin/env python

import sys
box_ids = []

def compare(a, b):
    match = ''
    diff = 0

    for index, char in enumerate(a, 0):
        if char == b[index]:
            match += char
        else:
            diff += 1

    return match if diff == 1 else None

for line in sys.stdin:
    box_ids.append(line.strip())

for pos1 in range(0, len(box_ids)):
    for pos2 in range(pos1 + 1, len(box_ids)):
        match = compare(box_ids[pos1], box_ids[pos2])
        if match:
            print(match)
            sys.exit(0)
