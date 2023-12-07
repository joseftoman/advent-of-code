#!/usr/bin/python3

import sys

favnum = 1350
queue = [ (1, 1, 0) ]
known = set(["1.1"])
reach = 0
max_step = 50

def is_wall(x, y):
    bits = [ bit for bit in list(bin((x + y)**2 + 3 * x + y + favnum)[2:]) if bit == '1' ]
    return True if len(bits) % 2 == 1 else False

def test_coords(x, y):
    if x < 0 or y < 0: return False

    flat = str(x)+'.'+str(y)

    if flat in known: return False
    if is_wall(x, y):
        #print("Wall:", x, y)
        known.add(flat)
        return False

    return True

def get_next(x, y):
    next = []

    for diff in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        new_x = x + diff[0]
        new_y = y + diff[1]
        if test_coords(new_x, new_y): next.append((new_x, new_y))

    return next

while queue:
    state = queue.pop(0)
    if state[2] > max_step:
        print(reach)
        break

    reach += 1
    #print("Pos: ", state)
    for next in get_next(state[0], state[1]):
        known.add(str(next[0])+'.'+str(next[1]))
        queue.append((next[0], next[1], state[2] + 1))
