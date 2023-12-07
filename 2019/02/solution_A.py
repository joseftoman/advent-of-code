#!/usr/bin/env python

import sys

program = [int(_) for _ in next(sys.stdin).strip().split(',')]
pos = 0
program[1] = 12
program[2] = 2

while True:
    op = program[pos]
    if op == 99:
        print(program[0])
        break

    arg1 = program[program[pos + 1]]
    arg2 = program[program[pos + 2]]
    dest = program[pos + 3]

    if op == 1:
        program[dest] = arg1 + arg2
    elif op == 2:
        program[dest] = arg1 * arg2
    else:
        print("Invalid op")
        break

    pos += 4
