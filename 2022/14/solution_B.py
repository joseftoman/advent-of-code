#!/usr/bin/env python

import sys

cave = {}
max_y = -1
source = (500, 0)
sand = 0

def print_cave():
    global cave
    global max_y

    points = sorted(list(cave), key=lambda p: p[0])
    min_x = points[0][0]
    max_x = points[-1][0]

    for y in range(max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) == source:
                print('+', end='')
                continue
            print(cave[(x, y)] if (x, y) in cave else '.', end='')
        print()
    print()


for index, line in enumerate(sys.stdin):
    points = [[int(coord) for coord in point.split(',')] for point in line.strip().split(' -> ')]
    cave[tuple(points[0])] = '#'
    pos = points[0]
    if pos[1] > max_y:
        max_y = pos[1]

    for point in points[1:]:
        if pos[0] == point[0]:
            diff = [0, 1 if point[1] > pos[1] else -1]
        else:
            diff = [1 if point[0] > pos[0] else -1, 0]

        while True:
            pos = [pos[0] + diff[0], pos[1] + diff[1]]
            cave[tuple(pos)] = '#'
            if pos[1] > max_y:
                max_y = pos[1]
            if pos == point:
                break

while True:
    pos = list(source)
    at_rest = False
    
    while not at_rest:
        if pos[1] == max_y + 1:
            at_rest = True
        else:
            if (pos[0], pos[1] + 1) not in cave:
                pos[1] += 1
            elif (pos[0] - 1, pos[1] + 1) not in cave:
                pos[0] -= 1
                pos[1] += 1
            elif (pos[0] + 1, pos[1] + 1) not in cave:
                pos[0] += 1
                pos[1] += 1
            else:
                at_rest = True
    
    cave[tuple(pos)] = 'o'
    sand += 1

    if tuple(pos) == source:
        break

print(sand)
