#!/usr/bin/python3

import sys
import string

maze = []
steps = 1
pos = None
diff = []

maze = [ l.rstrip() for l in sys.stdin ]

start = maze[0].find('|')
if start >= 0:
    pos = [0, start]
    diff = [1, 0]
else:
    start = maze[-1].find('|')
    if start >= 0:
        pos = [len(maze) - 1, start]
        diff = [-1, 0]
    else:
        for i in range(0, len(maze)):
            if maze[i][0] == '-':
                pos = [i, 0]
                diff = [0, 1]
                break
            elif maze[i][-1] == '-':
                pos = [i, len(maze[i])]
                diff = [0, -1]
                break

while True:
    prev = pos[:]
    pos[0] += diff[0]
    pos[1] += diff[1]

    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(maze) or pos[1] >= len(maze[pos[0]]): break
    if maze[pos[0]][pos[1]] == ' ': break
    steps += 1

    if maze[pos[0]][pos[1]] == '+':
        diff = None
        for new_diff in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_pos = [pos[0] + new_diff[0], pos[1] + new_diff[1]]
            if new_pos == prev: continue
            if new_pos[0] < 0 or new_pos[0] >= len(maze) or new_pos[1] < 0 or new_pos[1] >= len(maze[new_pos[0]]): continue
            if maze[new_pos[0]][new_pos[1]] != ' ':
                diff = new_diff
    
    if diff is None: break

print(steps)
