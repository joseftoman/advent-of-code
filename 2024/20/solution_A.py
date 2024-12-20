#!/usr/bin/env python

import sys

CHEAT_TARGET = 100


def main():
    race_map = {}
    path = []
    end = (0, 0)
    step = 0
    good_cheats = 0

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        for x, char in enumerate(line):
            race_map[(y, x)] = char
            if char == 'S':
                path.append((y, x))
                race_map[(y, x)] = step
            elif char == 'E':
                end = (y, x)
                race_map[(y, x)] = '.'

    while path[-1] != end:
        step += 1
        for diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            next_pos = (path[-1][0] + diff[0], path[-1][1] + diff[1])
            if race_map[next_pos] == '.':
                path.append(next_pos)
                race_map[next_pos] = step
                break

    for pos in path:
        for diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            cheat = (pos[0] + diff[0], pos[1] + diff[1])
            if race_map[cheat] == '#':
                cheat = (cheat[0] + diff[0], cheat[1] + diff[1])
                if isinstance(race_map.get(cheat), int) and race_map[cheat] - race_map[pos] - 2 >= CHEAT_TARGET:
                    good_cheats += 1

    print(good_cheats)


if __name__ == '__main__':
    main()
