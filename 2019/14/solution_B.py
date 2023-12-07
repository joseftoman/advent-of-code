#!/usr/bin/env python

from collections import defaultdict
import math
import sys

CARGO = 10 ** 12

def read_input():
    recipies = {}

    for line in sys.stdin:
        left, right = line.strip().split(' => ')
        ingredients = []

        for item in left.split(','):
            amount, unit = item.strip().split()
            ingredients.append([int(amount), unit])

        amount, unit = right.split()
        recipies[unit] = {'amount': int(amount), 'ingredients': ingredients}

    return recipies

def produce_fuel(repicies, amount):
    ore = CARGO
    need = defaultdict(int)
    need['FUEL'] = amount
    have = defaultdict(int)

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
                ore -= required
                continue

            h = min(required, have[ingredient[1]])
            required -= h
            have[ingredient[1]] -= h

            if required:
                need[ingredient[1]] += required

        if factor * recipies[unit]['amount'] > amount:
            have[unit] = factor * recipies[unit]['amount'] - amount

    return ore

recipies = read_input()
single_fuel = CARGO - produce_fuel(recipies, 1)
to_test = math.floor(CARGO / single_fuel)
low = None
high = None

while high is None or low is None or high > low + 1:
    diff = produce_fuel(recipies, to_test)

    if not diff:
        low = to_test
        high = to_test + 1
    if diff > 0:
        low = to_test
        to_test += max(1, math.floor(diff / single_fuel))
    if diff < 0:
        high = to_test
        to_test += math.floor(diff / single_fuel)

print(low)
