#!/usr/bin/env python

from collections import defaultdict
import sys

around = {'NW': (-1, -1), 'N': (-1, 0), 'NE': (-1, 1), 'W': (0, -1), 'E': (0, 1), 'SW': (1, -1), 'S': (1, 0), 'SE': (1, 1)}
steps = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}


def get_size(elves):
    size = list(next(iter(elves)))
    size = [size[0], size[1], size[0], size[1]]

    for elf in elves:
        if elf[0] < size[0]:
            size[0] = elf[0]
        if elf[0] > size[2]:
            size[2] = elf[0]
        if elf[1] < size[1]:
            size[1] = elf[1]
        if elf[1] > size[3]:
            size[3] = elf[1]

    return size


def print_elves(elves):
    size = get_size(elves)
    
    for row in range(size[0], size[2] + 1):
        for col in range(size[1], size[3] + 1):
            print('#' if (row, col) in elves else '.', end='')
        print()
    print()


def run_round(elves, dirs):
    moves = defaultdict(set)
    new_elves = set()
    movement = False

    for elf in elves:
        empty = {_: True for _ in dirs}

        for direction, coords in around.items():
            pos = (elf[0] + coords[0], elf[1] + coords[1])
            if pos not in elves:
                continue
            for target in list(direction):
                empty[target] = False

        if all(empty.values()):
            new_elves.add(elf)
            continue
   
        has_option = False
        for target in dirs:
            if empty[target]:
                pos = (elf[0] + around[target][0], elf[1] + around[target][1])
                moves[pos].add(elf)
                has_option = True
                break

        if not has_option:
            new_elves.add(elf)

    for pos, applicants in moves.items():
        if len(applicants) == 1:
            new_elves.add(pos)
            movement = True
        else:
            new_elves |= applicants

    return new_elves if movement else None


def main():
    elves = set()
    dirs = ['N', 'S', 'W', 'E']

    for row, line in enumerate(sys.stdin):
        for col, char in enumerate(line.strip()):
            if char == '#':
                elves.add((row, col))

    round_no = 0
    while True:
        round_no += 1
        elves = run_round(elves, dirs)
        dirs = dirs[1:] + [dirs[0]]
        if elves is None:
            break
        #print_elves(elves)

    print(round_no)


if __name__ == '__main__':
    main()
