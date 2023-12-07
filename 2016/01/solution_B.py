#!/usr/bin/python3

import sys

directions = sys.stdin.readline().rstrip()
pos = [0, 0]
facing = 0
steps = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
plan = {}

for step in directions.split(", "):
    print("Step:", step)
    if step[0] == 'R':
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4

    for coord in range(0, 2):
        if steps[facing][coord] == 0: continue

        for i in range(0, int(step[1:])):
            pos[coord] += steps[facing][coord]
            print("- pos:", pos)

            if pos[0] in plan and pos[1] in plan[pos[0]]:
                print(abs(pos[0]) + abs(pos[1]))
                exit()
            else:
                if pos[0] not in plan: plan[pos[0]] = {}
                if pos[1] not in plan[pos[0]]: plan[pos[0]][pos[1]] = 1
