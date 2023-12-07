#!/usr/bin/env python

import itertools
import sys

def run_program(program, phase_setting, input_signal):
    program = program[:]
    pos = 0
    input_stack = [input_signal, phase_setting]

    while True:
        op = program[pos] % 100
        modes = f'{program[pos] // 100:03d}'[::-1]

        if op == 99:
            print('HALT')
            sys.exit(1)

        args = []
        args_count = 0
        dest = None
        shift = None
        skip = False

        if op in (1, 2, 7, 8):
            args_count = 2
            dest = program[pos + 3]
            shift = 4
        elif op == 3:
            dest = program[pos + 1]
            shift = 2
        elif op == 4:
            args_count = 1
            shift = 2
        elif op in (5, 6):
            args_count = 2
            shift = 3

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
            program[dest] = input_stack.pop()
        elif op == 4:
            return args[0]
        elif op == 5:
            if args[0]:
                pos = args[1]
                skip = True
        elif op == 6:
            if not args[0]:
                pos = args[1]
                skip = True
        elif op == 7:
            program[dest] = 1 if args[0] < args[1] else 0
        elif op == 8:
            program[dest] = 1 if args[0] == args[1] else 0
        else:
            print("Invalid op")
            sys.exit(1)

        if not skip:
            pos += shift

program = [int(_) for _ in next(sys.stdin).strip().split(',')]
cache = dict()
best = None

for p in itertools.permutations(range(5)):
    signal = 0

    for amp in range(5):
        key = (p[amp], signal)
        if key in cache:
            signal = cache[key]
        else:
            signal = run_program(program, *key)
            cache[key] = signal

    if best is None or signal > best:
        best = signal
        print('MAX:', best, p)

print(best)
