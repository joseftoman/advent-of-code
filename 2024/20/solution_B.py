#!/usr/bin/env python

import sys

CHEAT_LEN = 20
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
        for y_diff in range(CHEAT_LEN + 1):
            for x_diff in range(CHEAT_LEN - y_diff + 1):
                if y_diff + x_diff < 2:
                    continue

                for cheat_end in list({
                    (pos[0] - y_diff, pos[1] - x_diff),
                    (pos[0] - y_diff, pos[1] + x_diff),
                    (pos[0] + y_diff, pos[1] - x_diff),
                    (pos[0] + y_diff, pos[1] + x_diff),
                }):
                    if isinstance(race_map.get(cheat_end), int) and race_map[cheat_end] - race_map[pos] - y_diff - x_diff >= CHEAT_TARGET:
                        good_cheats += 1

    print(good_cheats)


if __name__ == '__main__':
    main()
