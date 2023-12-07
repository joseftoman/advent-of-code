#!/usr/bin/python3

import sys
import re

program = []
r = {}
pos = 0
count = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    i = line.split(' ')
    program.append(i)
    for arg in (0, 1):
        if i[arg].isalpha and i[arg] not in r: r[i[arg]] = 0

def get_val(arg):
    return r[arg] if arg.isalpha() else int(arg)

while pos >= 0 and pos < len(program):
    i = program[pos]
    c = i[0]

    if c == 'set':
        r[i[1]] = get_val(i[2])
    elif c == 'sub':
        r[i[1]] -= get_val(i[2])
    elif c == 'mul':
        r[i[1]] *= get_val(i[2])
        count += 1
    elif c == 'jnz':
        if get_val(i[1]) != 0:
            pos += get_val(i[2])
            continue

    pos += 1

print(count)
