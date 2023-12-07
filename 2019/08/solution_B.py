#!/usr/bin/env python

import sys

width = 25
height = 6
layer_index = 0
layer_size = width * height
image = ['2'] * width * height

data = next(sys.stdin).rstrip()

while layer_index * layer_size < len(data):
    for pos in range(layer_size):
        if image[pos] == '2':
            image[pos] = data[layer_index * layer_size + pos]

    layer_index += 1

for row in range(0, height):
    print(''.join(['*' if _ == '1' else ' ' for _ in image[row * width:(row + 1) * width]]))
