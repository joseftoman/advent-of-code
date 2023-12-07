#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} INPUT_NUMBER')
    sys.exit(1)

few = int(sys.argv[1])

recipes = [3, 7]
elf1 = 0
elf2 = 1
result = 10

while len(recipes) < few + result:
    new = recipes[elf1] + recipes[elf2]
    if new >= 10:
        recipes.append(new // 10)
    recipes.append(new % 10)
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print(''.join([str(r) for r in recipes[few:few+result]]))
