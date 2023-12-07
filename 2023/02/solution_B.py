#!/usr/bin/env python

import sys

color_mapping = {'red': 0, 'green': 1, 'blue': 2}
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
    min_set = [0, 0, 0]

    for hand in hands:
        for color in range(3):
            min_set[color] = max(min_set[color], hand[color])

    total += min_set[0] * min_set[1] * min_set[2]

print(total)
