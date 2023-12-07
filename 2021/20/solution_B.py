#!/usr/bin/env python

import sys

def render(image, borders):
    for y in range(borders[2], borders[3] + 1):
        line = ''
        for x in range(borders[0], borders[1] + 1):
            line += '#' if image.get((x, y)) == '1' else '.'
        print(line)

    print(len(image))

algo = sys.stdin.readline().rstrip()
sys.stdin.readline()

borders = [0, 0, 0, 0]
image = {}

for y, line in enumerate(sys.stdin):
    for x, pixel in enumerate(list(line.rstrip())):
        if pixel != '#':
            continue
        image[(x, y)] = '1'
        if x < borders[0]:
            borders[0] = x
        if x > borders[1]:
            borders[1] = x
        if y < borders[2]:
            borders[2] = y
        if y > borders[3]:
            borders[3] = y

for loop in range(50):
    new_image = {}
    new_borders = [None, None, None, None]
    for x in range(borders[0] - 1, borders[1] + 2):
        for y in range(borders[2] - 1, borders[3] + 2):
            square = ''
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    pixel = (x + dx, y + dy)
                    if algo[0] == '#' and (pixel[0] < borders[0] or pixel[0] > borders[1] or pixel[1] < borders[2] or pixel[1] > borders[3]):
                        square += '1' if loop % 2 else '0'
                    else:
                        square += image.get((x + dx, y + dy), '0')
            if algo[int(square, 2)] == '#':
                new_image[(x, y)] = '1'
                if new_borders[0] is None or x < new_borders[0]:
                    new_borders[0] = x
                if new_borders[1] is None or x > new_borders[1]:
                    new_borders[1] = x
                if new_borders[2] is None or y < new_borders[2]:
                    new_borders[2] = y
                if new_borders[3] is None or y > new_borders[3]:
                    new_borders[3] = y

    borders = new_borders
    image = new_image

print(len(image))
