#!/usr/bin/env python

import sys


def get_pos(square, move):
    return square[0] + move[0], square[1] + move[1]


def get_moves():
    for line in sys.stdin:
        for char in line.strip():
            yield char, {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}[char]


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
            w_char = {'@': '@.', '.': '..', '#': '##', 'O': '[]'}[char]
            warehouse[(y, 2 * x)] = w_char[0]
            warehouse[(y, 2 * x + 1)] = w_char[1]
            if char == '@':
                robot = (y, 2 * x)

    # render(warehouse)

    for char, diff in get_moves():
        pos = get_pos(robot, diff)
        can_move = warehouse[pos] != '#'

        # Moving left and right is easy
        if char in {'<', '>'}:
            steps = 1

            while can_move and warehouse[pos] != '.':
                steps += 1
                pos = get_pos(pos, diff)
                if warehouse[pos] == '#':
                    can_move = False

            inverse_diff = (0, diff[1] * -1)

            if can_move:
                for _ in range(steps):
                    step_back = get_pos(pos, inverse_diff)
                    warehouse[pos] = warehouse[step_back]
                    pos = step_back
                warehouse[robot] = '.'
                robot = get_pos(robot, diff)

            # render(warehouse)
            continue

        edge = {robot}
        step_ahead = {pos}
        boxes = set()

        while can_move and any(warehouse[_] != '.' for _ in step_ahead):
            new_edge = set()
            for edge_pos in edge:
                next_pos = get_pos(edge_pos, diff)
                sidekick = None

                if warehouse[next_pos] == '.':
                    new_edge.add(edge_pos)
                    continue

                if warehouse[next_pos] == '[':
                    sidekick = get_pos(next_pos, (0, 1))
                elif warehouse[next_pos] == ']':
                    sidekick = get_pos(next_pos, (0, -1))

                boxes.add(next_pos)
                boxes.add(sidekick)
                new_edge.add(next_pos)
                new_edge.add(sidekick)

            step_ahead = {get_pos(_, diff) for _ in new_edge}
            edge = new_edge
            if any(warehouse[_] == '#' for _ in step_ahead):
                can_move = False

        if can_move:
            for box in sorted(boxes, reverse=char == 'v'):
                warehouse[get_pos(box, diff)] = warehouse[box]
                warehouse[box] = '.'
            warehouse[get_pos(robot, diff)] = '@'
            warehouse[robot] = '.'
            robot = get_pos(robot, diff)

        # render(warehouse)

    for pos, char in warehouse.items():
        if char == '[':
            total += 100 * pos[0] + pos[1]

    print(total)


if __name__ == '__main__':
    main()
