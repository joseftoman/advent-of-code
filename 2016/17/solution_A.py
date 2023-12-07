#!/usr/bin/python3

import hashlib

password = 'pxxbnzuo'
dim = (3, 3)
target = (3, 3)
queue = [ (0, 0, '') ]
door_open = set(['b', 'c', 'd', 'e', 'f'])

while queue:
    state = queue.pop(0)
    doors = list(hashlib.md5((password+state[2]).encode("utf-8")).hexdigest()[0:4])

    for diff in [(1, 0, 'R'), (-1, 0, 'L'), (0, 1, 'D'), (0, -1, 'U')]:
        if doors.pop() in door_open:
            next_state = (state[0] + diff[0], state[1] + diff[1], state[2] + diff[2])
            if next_state[0] < 0 or next_state[1] < 0 or next_state[0] > dim[0] or next_state[1] > dim[1]:
                continue
            if next_state[0] == target[0] and next_state[1] == target[1]:
                print(next_state[2])
                queue = []
                break

            queue.append(next_state)
