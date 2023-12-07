#!/usr/bin/env python

import heapq
import string
import sys

maze = {}
start = None
keys = set(string.ascii_lowercase)
doors = set(string.ascii_uppercase)
target = set()


def find_next_keys(robots, owned_keys):
    distances = {}

    for robot_no, start in enumerate(robots):
        sub_heap = [(0, start)]
        visited = set()

        while sub_heap:
            cost, pos = heapq.heappop(sub_heap)
            if pos in visited:
                continue
            visited.add(pos)

            for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_pos = (pos[0] + diff[0], pos[1] + diff[1])
                if next_pos not in maze or next_pos in visited or maze[next_pos] == '#' or (maze[next_pos] in doors and maze[next_pos].lower() not in owned_keys):
                    continue
                if maze[next_pos] in keys and maze[next_pos] not in owned_keys:
                    if distances.get(maze[next_pos], (cost + 2, ))[0] > cost + 1:
                        distances[maze[next_pos]] = (cost + 1, next_pos, robot_no)
                    continue

                heapq.heappush(sub_heap, (cost + 1, next_pos))

    return distances


for row, line in enumerate(sys.stdin):
    for col, mark in enumerate(line.strip()):
        if mark in keys:
            target.add(mark)
        if mark == '@':
            start = (row, col)
        maze[(row, col)] = mark

robots = []
maze[start] = '#'
for diff in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
    pos = (start[0] + diff[0], start[1] + diff[1])
    maze[pos] = '@'
    robots.append(pos)
for diff in ((0, -1), (0, 1), (-1, 0), (1, 0)):
    pos = (start[0] + diff[0], start[1] + diff[1])
    maze[pos] = '#'

heap = [(0, tuple(robots), set())]
visited = set()

while heap:
    cost, robots, owned_keys = heapq.heappop(heap)
    if (robots, tuple(sorted(owned_keys))) in visited:
        continue
    visited.add((robots, tuple(sorted(owned_keys))))

    if owned_keys == target:
        print(cost)
        break

    for key, path_info in find_next_keys(robots, owned_keys).items():
        new_keys = owned_keys | {key}
        new_robots = list(robots)
        new_robots[path_info[2]] = path_info[1]
        new_robots = tuple(new_robots)
        if (new_robots, tuple(sorted(new_keys))) in visited:
            continue
        heapq.heappush(heap, (cost + path_info[0], new_robots, new_keys))
