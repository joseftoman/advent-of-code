#!/usr/bin/env python

import sys

color_mapping = {'red': 0, 'green': 1, 'blue': 2}
limit = [12, 13, 14]
total = 0


def games():
    for line in sys.stdin:
        name, text = [_.strip() for _ in line.split(':')]

        _, number = name.split()

        hands = []

        for hand in text.split(';'):
            cubes = [0, 0, 0]
            for cube in hand.split(','):
                amount, color = cube.split()
                cubes[color_mapping[color]] += int(amount)
            hands.append(cubes)

        yield int(number), hands
        

for number, hands in games():
    possible = True

    for hand in hands:
        for color in range(3):
            if hand[color] > limit[color]:
                possible = False
                break
        if not possible:
            break

    if possible:
        total += number

print(total)
