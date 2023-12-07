#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} INPUT_SEQUENCE')
    sys.exit(1)

target = sys.argv[1]

recipes = [3, 7]
elf1 = 0
elf2 = 1

def is_match(r, t):
    return ''.join([str(x) for x in r[-len(t):]]) == t

while True:
    new = recipes[elf1] + recipes[elf2]

    if new >= 10:
        recipes.append(new // 10)
        if is_match(recipes, target):
            break

    recipes.append(new % 10)
    if is_match(recipes, target):
        break

    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print(len(recipes) - len(target))
