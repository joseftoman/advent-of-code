#!/usr/bin/python3

import sys

directions = sys.stdin.readline().rstrip()
pos = [0, 0]
facing = 0
steps = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
plan = {}

for step in directions.split(", "):
    if step[0] == 'R':
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4
    
    pos[0] += steps[facing][0] * int(step[1:])
    pos[1] += steps[facing][1] * int(step[1:])
    #print(step + ":", pos)

print(abs(pos[0]) + abs(pos[1]))
