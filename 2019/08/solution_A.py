#!/usr/bin/env python

import sys

width = 25
height = 6
layer_index = 0
layer_size = width * height


data = next(sys.stdin).rstrip()
best = None

while layer_index * layer_size < len(data):
    digits = {str(_): 0 for _ in range(0, 10)}
    for pos in range(layer_size):
        digits[data[layer_index * layer_size + pos]] += 1

    if best is None or digits['0'] < best[0]:
        best = (digits['0'], digits['1'] * digits['2'])

    layer_index += 1

print(best[1])
