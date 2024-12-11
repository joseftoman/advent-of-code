#!/usr/bin/env python

import sys


stones = [int(_) for _ in next(sys.stdin).split()]
for _ in range(25):
    after_blink = []
    for stone in stones:
        if stone == 0:
            after_blink.append(1)
        elif len(label := str(stone)) % 2 == 0:
            after_blink.extend([int(label[:len(label) // 2]), int(label[len(label) // 2:])])
        else:
            after_blink.append(stone * 2024)

    stones = after_blink

print(len(stones))
