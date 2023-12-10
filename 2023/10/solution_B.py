#!/usr/bin/env python

from collections import deque
import math
import sys

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

IN = 'in'
OUT = 'out'

moves = {
    '|': {UP: UP, DOWN: DOWN},
    '-': {LEFT: LEFT, RIGHT: RIGHT},
    'L': {DOWN: RIGHT, LEFT: UP},
    'J': {DOWN: LEFT, RIGHT: UP},
    '7': {RIGHT: DOWN, UP: LEFT},
    'F': {LEFT: DOWN, UP: RIGHT},
}

in_plains = {
    'L': {
        DOWN: {LEFT: OUT, RIGHT: IN},
        LEFT: {UP: IN, DOWN: OUT},
    },
    'J': {
        DOWN: {LEFT: IN, RIGHT: OUT},
        RIGHT: {UP: IN, DOWN: OUT},
    },
    '7': {
        UP: {LEFT: IN, RIGHT: OUT},
        RIGHT: {UP: OUT, DOWN: IN},
    },
    'F': {
        UP: {LEFT: OUT, RIGHT: IN},
        LEFT: {UP: OUT, DOWN: IN},
    },
}

out_plains = {
    'L': {
        UP: {IN: RIGHT, OUT: LEFT},
        RIGHT: {IN: UP, OUT: DOWN},
    },
    'J': {
        UP: {IN: LEFT, OUT: RIGHT},
        LEFT: {IN: UP, OUT: DOWN},
    },
    '7': {
        DOWN: {IN: LEFT, OUT: RIGHT},
        LEFT: {IN: DOWN, OUT: UP},
    },
    'F': {
        DOWN: {IN: RIGHT, OUT: LEFT},
        RIGHT: {IN: DOWN, OUT: UP},
    },
}

outside = {
    '|': {LEFT: [LEFT], RIGHT: [RIGHT]},
    '-': {UP: [UP], DOWN: [DOWN]},
    'L': {IN: [], OUT: [LEFT, DOWN]},
    'J': {IN: [], OUT: [RIGHT, DOWN]},
    '7': {IN: [], OUT: [RIGHT, UP]},
    'F': {IN: [], OUT: [LEFT, UP]},
}

def check_next_step(area, pos, max_y, max_x, step):
    ny, nx = pos[0] + step[0], pos[1] + step[1]
    if ny < 0 or ny == max_y:
        return None
    if nx < 0 or nx == max_x:
        return None

    char = area[ny][nx]
    next_step = moves.get(char, {}).get(step)
    if next_step is None and char != 'S':
        return None
    return (ny, nx), next_step


def initial_steps(area, pos, max_y, max_x):
    for step in [UP, DOWN, LEFT, RIGHT]:
        next_step = check_next_step(area, pos, max_y, max_x, step)
        if next_step is not None:
            yield pos, step


def find_loop(area, start, max_y, max_x):
    tails = [[_] for _ in initial_steps(area, start, max_y, max_x)]

    while True:
        new_tails = []
        for tail in tails:
            pos, step = tail[-1]
            next_step = check_next_step(area, pos, max_y, max_x, step)
            if next_step is not None:
                if next_step[1] is not None:
                    tail.append(next_step)
                    new_tails.append(tail)
                else:
                    area[start[0]][start[1]] = {
                        (DOWN, DOWN): '|',
                        (UP, UP): '|',
                        (LEFT, LEFT): '-',
                        (RIGHT, RIGHT): '-',
                        (DOWN, RIGHT): 'L',
                        (LEFT, UP): 'L',
                        (DOWN, LEFT): 'J',
                        (RIGHT, UP): 'J',
                        (RIGHT, DOWN): '7',
                        (UP, LEFT): '7',
                        (LEFT, DOWN): 'F',
                        (UP, RIGHT): 'F',
                    }[(step, tail[0][1])]

                    loop = {_[0] for _ in tail}
                    for y in range(max_y):
                        for x in range(max_x):
                            if (y, x) not in loop:
                                area[y][x] = '.' 

                    return tail


def main():
    area = [list(_.strip()) for _ in sys.stdin]
    for y, line in enumerate(area):
        if y == 0:
            max_x = len(line)
        for x, char in enumerate(line):
            if char == 'S':
                start = y, x
    max_y = len(area)

    loop = find_loop(area, start, max_y, max_x)
    
    x = 0
    while area[start[0]][x] == '.':
        x += 1
    pos = (start[0], x)
    
    for index, pipe in enumerate(loop):
        if pipe[0] == pos:
            break

    loop = loop[index:] + loop[:index]
    plain = {'|': LEFT, 'L': OUT, 'F': OUT}[area[pos[0]][pos[1]]]
    prev_step = None

    queue = deque()
    visited = set()

    for pipe in loop:
        y, x = pipe[0]
        if prev_step is not None:
            plain = in_plains.get(area[y][x], {}).get(prev_step, {}).get(plain, plain)
        for diff in outside[area[y][x]][plain]:
            ny, nx = y + diff[0], x + diff[1]
            if 0 <= ny < max_y and 0 <= nx < max_x and area[ny][nx] == '.' and (ny, nx) not in visited:
                queue.append((ny, nx))
                visited.add((ny, nx))
                area[ny][nx] = 'O'
        plain = out_plains.get(area[y][x], {}).get(pipe[1], {}).get(plain, plain)
        prev_step = pipe[1]

    while queue:
        y, x = queue.popleft()
        for dy, dx in [LEFT, RIGHT, UP, DOWN]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < max_y and 0 <= nx < max_x and area[ny][nx] == '.' and (ny, nx) not in visited:
                queue.append((ny, nx))
                visited.add((ny, nx))
                area[ny][nx] = 'O'

    print(max_y * max_x - len(loop) - len(visited))


if __name__ == '__main__':
    main()
