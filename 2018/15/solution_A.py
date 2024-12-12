#!/usr/bin/env python

import sys

HIT_POINTS = 200
ATTACK_POWER = 3

MOVES = ((-1, 0), (0, -1), (0, 1), (1, 0))


def get_pos(square, move):
    return square[0] + move[0], square[1] + move[1]


def get_adjacent(pos):
    for move in MOVES:
        yield get_pos(pos, move)


def find_enemy_in_range(unit, enemies):
    target = None

    for pos in get_adjacent(unit):
        if pos in enemies and (target is None or enemies[pos][0] < enemies[target][0]):
            target = pos

    return target


def get_next_move(unit, cave, enemies):
    targets = set()

    for enemy in enemies.keys():
        for pos in get_adjacent(enemy):
            if cave.get(pos) == '.':
                targets.add(pos)

    current_positions = []
    seen = set()

    for pos in get_adjacent(unit):
        if pos in targets:
            return pos
        if cave.get(pos) == '.' and pos not in seen:
            current_positions.append((pos, pos))
            seen.add(pos)

    while current_positions:
        next_positions = []
        targets_reached = {}

        for pos, first_step in current_positions:
            for next_pos in get_adjacent(pos):
                if next_pos in targets and next_pos not in targets_reached:
                    targets_reached[next_pos] = first_step
                if cave.get(next_pos) == '.' and next_pos not in seen:
                    next_positions.append((next_pos, first_step))
                    seen.add(next_pos)

        if targets_reached:
            return targets_reached[min(targets_reached.keys())]

        current_positions = next_positions

    return None


def render(step, cave, elves, goblins):
    units = {**elves, **goblins}
    max_y = max(_[0] for _ in cave.keys())
    max_x = max(_[1] for _ in cave.keys())

    if step is None:
        print('\nFinish:')
    elif step == 0:
        print('Initially:')
    else:
        print(f'\nFinished rounds: {step}')

    for y in range(max_y + 2):
        health = []

        for x in range(max_x + 2):
            char = cave.get((y, x), '#')
            print(char, end='')
            if char in {'E', 'G'}:
                health.append(units[(y, x)][0])

        print(''.join(f'{_:4}' for _ in health), end='')
        print('')


def main():
    cave = {}
    elves = {}
    goblins = {}
    step = 0
    next_unit_id = 1

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        for x, square in enumerate(line):
            if square in {'.', 'E', 'G'}:
                cave[(y, x)] = square
            if square == 'E':
                elves[(y, x)] = [HIT_POINTS, next_unit_id]
                next_unit_id += 1
            elif square == 'G':
                goblins[(y, x)] = [HIT_POINTS, next_unit_id]
                next_unit_id += 1

    # render(step, cave, elves, goblins)

    while True:
        finish = False

        for unit, id_check in [(pos, elves.get(pos, goblins.get(pos))[1]) for pos in sorted([*elves.keys(), *goblins.keys()])]:
            if cave[unit] == '.' or (goblins[unit][1] if cave[unit] == 'G' else elves[unit][1]) != id_check:
                # The unit scheduled to take its turn had been killed and (optionally) another unit has moved into its original position.
                continue

            enemies = elves if cave[unit] == 'G' else goblins
            friends = goblins if cave[unit] == 'G' else elves

            if not enemies:
                finish = True
                break

            enemy = find_enemy_in_range(unit, enemies)
            if not enemy:
                pos = get_next_move(unit, cave, enemies)
                if pos is not None:
                    friends[pos] = friends.pop(unit)
                    cave[pos] = cave[unit]
                    cave[unit] = '.'
                    unit = pos

            enemy = find_enemy_in_range(unit, enemies)
            if enemy is not None:
                enemies[enemy][0] -= ATTACK_POWER
                if enemies[enemy][0] <= 0:
                    del enemies[enemy]
                    cave[enemy] = '.'

        if finish:
            break

        step += 1
        # render(step, cave, elves, goblins)

    # render(None, cave, elves, goblins)
    print(step * sum(_[0] for _ in [*elves.values(), *goblins.values()]))


if __name__ == '__main__':
    main()
