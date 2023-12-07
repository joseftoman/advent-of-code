#!/usr/bin/env python

import sys

def read_wire(callback):
    pos = [0, 0]

    for bend in [(item[0], int(item[1:])) for item in next(sys.stdin).strip().split(',')]:
        for _ in range(0, bend[1]):
            if bend[0] == 'U':
                pos[1] += 1
            elif bend[0] == 'D':
                pos[1] -= 1
            elif bend[0] == 'L':
                pos[0] -= 1
            elif bend[0] == 'R':
                pos[0] += 1

            callback(tuple(pos))

wire = set()
best = None
read_wire(lambda pos: wire.add(pos))

def check_crossing(pos):
    global best
    global wire

    if pos not in wire:
        return

    dist = abs(pos[0]) + abs(pos[1])
    if best is None or dist < best:
        best = dist

read_wire(check_crossing)

print(best)
