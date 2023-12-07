#!/usr/bin/env python

import sys

input_program = [int(_) for _ in next(sys.stdin).strip().split(',')]
target = 19690720

for a in range(0, 100):
    for b in range(0, 100):
        program = input_program[:]
        program[1] = a
        program[2] = b
        pos = 0

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

        print(a, b, program[0])

        if program[0] == target:
            print('RESULT:', 100 * a + b)
            sys.exit(0)
