#!/usr/bin/env python

import sys


def get_pos(square, move):
    return square[0] + move[0], square[1] + move[1]


def get_moves():
    for line in sys.stdin:
        for char in line.strip():
            yield {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}[char]


def render(warehouse):
    max_y = max(_[0] for _ in warehouse)
    max_x = max(_[1] for _ in warehouse)
    for y in range(max_y + 1):
        print(''.join(warehouse[(y, x)] for x in range(max_x + 1)))
    print()


def main():
    warehouse = {}
    robot = None
    total = 0

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        if not line:
            break
        for x, char in enumerate(line):
            warehouse[(y, x)] = char
            if char == '@':
                robot = (y, x)

    # render(warehouse)

    for move in get_moves():
        pos = get_pos(robot, move)
        can_move = warehouse[pos] != '#'
        steps = 1

        while can_move and warehouse[pos] != '.':
            steps += 1
            pos = get_pos(pos, move)
            if warehouse[pos] == '#':
                can_move = False

        inverse_move = (move[0] * -1, move[1] * -1)

        if can_move:
            for _ in range(steps):
                step_back = get_pos(pos, inverse_move)
                warehouse[pos] = warehouse[step_back]
                pos = step_back
            warehouse[robot] = '.'
            robot = get_pos(robot, move)

        # render(warehouse)

    for pos, char in warehouse.items():
        if char == 'O':
            total += 100 * pos[0] + pos[1]

    print(total)


if __name__ == '__main__':
    main()
