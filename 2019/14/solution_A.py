#!/usr/bin/env python

from collections import defaultdict
import math
import sys

need = defaultdict(int)
need['FUEL'] = 1
ore = 0
have = defaultdict(int)
recipies = {}

for line in sys.stdin:
    left, right = line.strip().split(' => ')
    ingredients = []

    for item in left.split(','):
        amount, unit = item.strip().split()
        ingredients.append([int(amount), unit])

    amount, unit = right.split()
    recipies[unit] = {'amount': int(amount), 'ingredients': ingredients}

while need:
    unit, amount = need.popitem()
    h = min(amount, have[unit])
    amount -= h
    have[unit] -= h
    if not amount:
        continue

    factor = math.ceil(amount / recipies[unit]['amount'])

    for ingredient in recipies[unit]['ingredients']:
        required = factor * ingredient[0]
        if ingredient[1] == 'ORE':
            ore += required
            continue

        h = min(required, have[ingredient[1]])
        required -= h
        have[ingredient[1]] -= h

        if required:
            need[ingredient[1]] += required

    if factor * recipies[unit]['amount'] > amount:
        have[unit] = factor * recipies[unit]['amount'] - amount

print(ore)
