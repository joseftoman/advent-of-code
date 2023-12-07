#!/usr/bin/env python

from enum import Enum
import math
import re
import sys


class S(Enum):
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'

    def __int__(self):
        return {'>': 0, 'v': 1, '<': 2, '^': 3}[self.value]

    def __add__(self, other):
        # For cube walking. Change of direction of movement based on area rotation.
        # We are supposed to walk in a certain direction. What's going to be the actual
        # direction given the cube face's rotation in the input.
        if not isinstance(other, R):
            raise Exception()

        step_order = '>v<^'
        step_shift = {R.NONE: 0, R.LEFT: -1, R.RIGHT: 1, R.FLIP: 2}
        return S(step_order[(step_order.find(self.value) + step_shift[other]) % 4])


class R(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    FLIP = 'F'
    NONE = None

    def __add__(self, other):
        rotation_sums = {
            frozenset([R.LEFT, R.LEFT]): R.FLIP,
            frozenset([R.LEFT, R.RIGHT]): R.NONE,
            frozenset([R.LEFT, R.FLIP]): R.RIGHT,
            frozenset([R.LEFT, R.NONE]): R.LEFT,
            frozenset([R.RIGHT, R.RIGHT]): R.FLIP,
            frozenset([R.RIGHT, R.FLIP]): R.LEFT,
            frozenset([R.RIGHT, R.NONE]): R.RIGHT,
            frozenset([R.FLIP, R.FLIP]): R.NONE,
            frozenset([R.FLIP, R.NONE]): R.FLIP,
            frozenset([R.NONE, R.NONE]): R.NONE,
        }

        step_order = '>v<^'
        step_shift = {R.NONE: 0, R.LEFT: 1, R.RIGHT: -1, R.FLIP: 2}

        if isinstance(other, R):
            # Trivial adding of rotations
            return rotation_sums[frozenset([self, other])]
        if isinstance(other, S):
            # For cube folding. Having an arbitrarily rotated area and its adjacent area,
            # what is their relative position on a folded cube?
            # Left neighbour of an area rotated to the right is "below" on a cube.
            return S(step_order[(step_order.find(other.value) + step_shift[self]) % 4])
        raise Exception()


step_to_diff = {S.RIGHT: (0, 1), S.DOWN: (1, 0), S.LEFT: (0, -1), S.UP: (-1, 0)}

transitions = {
    1: {'>': [2, R(None)], 'v': [4, R(None)], '<': [5, R(None)], '^': [3, R(None)]},
    2: {'>': [6, R(None)], 'v': [4, R('L')], '<': [1, R(None)], '^': [3, R('R')]},
    3: {'>': [2, R('L')], 'v': [1, R(None)], '<': [5, R('R')], '^': [6, R('F')]},
    4: {'>': [2, R('R')], 'v': [6, R('F')], '<': [5, R('L')], '^': [1, R(None)]},
    5: {'>': [1, R(None)], 'v': [4, R('R')], '<': [6, R(None)], '^': [3, R('L')]},
    6: {'>': [5, R(None)], 'v': [4, R('F')], '<': [2, R(None)], '^': [3, R('F')]},
}


def fold_cube(lines):
    faces = {}
    chars = sum(map(lambda line: len(line.strip().replace(' ', '')), lines))
    edge_len = int(math.sqrt(chars // 6))
    width = max(len(_) for _ in lines) // edge_len
    height = len(lines) // edge_len

    col = lines[0].find('.') // edge_len
    if col < 0:
        col = lines[0].find('#') // edge_len
    stack = [(1, (0, col), R.NONE)]

    while stack:
        area = stack.pop()
        if area[0] in faces:
            continue

        faces[area[0]] = (area[1], area[2])

        for step, diff in step_to_diff.items():
            new_pos = (area[1][0] + diff[0], area[1][1] + diff[1])
            if not (0 <= new_pos[0] < height and 0 <= new_pos[1] < width):
                continue
            if len(lines[new_pos[0] * edge_len]) <= new_pos[1] * edge_len or lines[new_pos[0] * edge_len][new_pos[1] * edge_len] == ' ':
                continue

            adjacent = transitions[area[0]][(area[2] + step).value]
            if adjacent[0] in faces:
                continue

            stack.append((adjacent[0], new_pos, area[2] + adjacent[1]))

    return faces, edge_len


def flip_edge(current_facing, next_facing):
    args = sorted([int(current_facing), int(next_facing)])
    return args in [[0, 1], [0, 2], [1, 3], [2, 3]]


def walk_cube(lines, faces, edge_len, moves):
    faces_by_pos = {info[0]: face_no for face_no, info in faces.items()}
    row, col = [_ * edge_len for _ in faces[1][0]]
    map_facing = S.RIGHT

    for move in moves:
        if move in {'R', 'L'}:
            map_facing = (R('L') if move == 'R' else R('R')) + map_facing
            continue

        for _ in range(int(move)):
            row_diff, col_diff = step_to_diff[map_facing]
            next_row, next_col = row + row_diff, col + col_diff

            if 0 <= next_row < len(lines) and 0 <= next_col < len(lines[next_row]) and lines[next_row][next_col] != ' ':
                if lines[next_row][next_col] == '#':
                    break
                row, col = next_row, next_col
                continue

            current_face = faces_by_pos[(row // edge_len, col // edge_len)]
            cube_facing = faces[current_face][1] + map_facing
            next_face = transitions[current_face][cube_facing.value]
            next_map_facing = next_face[1] + cube_facing + faces[next_face[0]][1]

            edge_pos = (row if map_facing in {S.LEFT, S.RIGHT} else col) % edge_len
            if flip_edge(map_facing, next_map_facing):
                edge_pos = edge_len - edge_pos - 1

            next_row, next_col = [_ * edge_len for _ in faces[next_face[0]][0]]
            if next_map_facing == S.RIGHT:
                next_row += edge_pos
            elif next_map_facing == S.DOWN:
                next_col += edge_pos
            elif next_map_facing == S.LEFT:
                next_row += edge_pos
                next_col += edge_len - 1
            elif next_map_facing == S.UP:
                next_col += edge_pos
                next_row += edge_len - 1

            if lines[next_row][next_col] == '#':
                break
            row, col = next_row, next_col
            map_facing = next_map_facing

    return row, col, map_facing


def main():
    lines = []
    for line in sys.stdin:
        line = line.rstrip('\n\r')
        if not line:
            break
        lines.append(line)

    moves = re.findall(r'(\d+|[RL])', sys.stdin.readline().strip())

    faces, edge_len = fold_cube(lines)
    row, col, facing = walk_cube(lines, faces, edge_len, moves)

    print(1000 * (row + 1) + 4 * (col + 1) + int(facing))

if __name__ == '__main__':
    main()
