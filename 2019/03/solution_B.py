#!/usr/bin/env python

import sys

def read_wire(callback):
    pos = [0, 0]
    length = 0

    for bend in [(item[0], int(item[1:])) for item in next(sys.stdin).strip().split(',')]:
        for _ in range(0, bend[1]):
            length += 1

            if bend[0] == 'U':
                pos[1] += 1
            elif bend[0] == 'D':
                pos[1] -= 1
            elif bend[0] == 'L':
                pos[0] -= 1
            elif bend[0] == 'R':
                pos[0] += 1

            callback(tuple(pos), length)

wire = dict()
best = None

def store_wire(pos, length):
    global wire
    if pos not in wire:
        wire[pos] = length

read_wire(store_wire)

def check_crossing(pos, length):
    global best
    global wire

    if pos not in wire:
        return

    dist = wire[pos] + length
    if best is None or dist < best:
        best = dist

read_wire(check_crossing)

print(best)
