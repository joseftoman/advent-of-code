#!/usr/bin/env python

import sys

J_LEFT = -1
J_STRAIGHT = 0
J_RIGHT = 1

D_LEFT = 0
D_UP = 1
D_RIGHT = 2
D_DOWN = 3

vehicle_mapping = {
    '^': ('|', D_UP),
    'v': ('|', D_DOWN),
    '<': ('-', D_LEFT),
    '>': ('-', D_RIGHT)
}
curve_mapping = {
    r'/': {
        D_LEFT: D_DOWN,
        D_UP: D_RIGHT,
        D_RIGHT: D_UP,
        D_DOWN: D_LEFT
    },
    '\\' : {
        D_LEFT: D_UP,
        D_UP: D_LEFT,
        D_RIGHT: D_DOWN,
        D_DOWN: D_RIGHT
    }
}

plan = {}
vehicles = []
crash = False

for row, line in enumerate(sys.stdin):
    for column, char in enumerate(line.rstrip()):
        if char in ('^', 'v', '<', '>'):
            plan[(row, column)] = [vehicle_mapping[char][0], True]
            vehicles.append([vehicle_mapping[char][1], row, column, J_LEFT])
        else:
            plan[(row, column)] = [char, False]

while not crash:
    vehicles.sort(key=lambda v: v[1] * 1000 + v[2])
    for v in vehicles:
        if v[0] == D_UP:
            goto = (v[1]-1, v[2])
        elif v[0] == D_DOWN:
            goto = (v[1]+1, v[2])
        elif v[0] == D_LEFT:
            goto = (v[1], v[2]-1)
        elif v[0] == D_RIGHT:
            goto = (v[1], v[2]+1)

        if plan[goto][1]:
            print(f'{goto[1]},{goto[0]}')
            crash = True
            break
        
        plan[(v[1], v[2])][1] = False
        plan[goto][1] = True
        v[1] = goto[0]
        v[2] = goto[1]

        if plan[goto][0] in ('/', '\\'):
            v[0] = curve_mapping[plan[goto][0]][v[0]]
        elif plan[goto][0] == '+':
            v[0] = (v[0] + v[3]) % 4
            v[3] = ((v[3] + 2) % 3) - 1
