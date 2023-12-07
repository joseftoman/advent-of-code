#!/usr/bin/env python

import sys

program = [int(_) for _ in next(sys.stdin).strip().split(',')]
pos = 0
input_value = 1

while True:
    op = program[pos] % 100
    modes = f'{program[pos] // 100:03d}'[::-1]

    if op == 99:
        #print(program)
        break

    args = []
    args_count = 0
    dest = None
    shift = None
    if op in (1, 2):
        args_count = 2
        dest = program[pos + 3]
        shift = 4
    elif op == 3:
        dest = program[pos + 1]
        shift = 2
    elif op == 4:
        args_count = 1
        shift = 2

    for arg_pos in range(0, args_count):
        arg_val = program[pos + 1 + arg_pos]
        if modes[arg_pos] == '0':
            args.append(program[arg_val])
        else:
            args.append(arg_val)

    #print(program, op, args)

    if op == 1:
        program[dest] = args[0] + args[1]
    elif op == 2:
        program[dest] = args[0] * args[1]
    elif op == 3:
        program[dest] = input_value
    elif op == 4:
        print(f'OUTPUT [{pos}]: {args[0]}')
    else:
        print("Invalid op")
        break

    pos += shift
