#!/usr/bin/env python

import sys

HIT_POINTS = 200
GOBLIN_ATTACK_POWER = 3
MIN_ELVEN_ATTACK_POWER = 4

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


def solve(cave, elven_attack_power):
    step = 0
    next_unit_id = 1
    elves = {}
    goblins = {}

    for pos, square in cave.items():
        if square == 'E':
            elves[pos] = [HIT_POINTS, next_unit_id]
            next_unit_id += 1
        elif square == 'G':
            goblins[pos] = [HIT_POINTS, next_unit_id]
            next_unit_id += 1

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
                enemies[enemy][0] -= GOBLIN_ATTACK_POWER if cave[unit] == 'G' else elven_attack_power
                if enemies[enemy][0] <= 0:
                    if cave[unit] == 'G':
                        # An elf died
                        return None

                    del enemies[enemy]
                    cave[enemy] = '.'

        if finish:
            break

        step += 1

    return step * sum(_[0] for _ in [*elves.values(), *goblins.values()])


def main():
    cave = {}

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        for x, square in enumerate(line):
            if square in {'.', 'E', 'G'}:
                cave[(y, x)] = square

    elven_attack_power = MIN_ELVEN_ATTACK_POWER

    while True:
        output = solve(cave.copy(), elven_attack_power)
        if output is not None:
            print(output)
            return

        elven_attack_power += 1


if __name__ == '__main__':
    main()
