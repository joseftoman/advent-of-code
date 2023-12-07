#!/usr/bin/env python

import sys

class HaltException(Exception):
    pass

class NoInputException(Exception):
    pass

class ICC():
    def __init__(self, program, *args):
        self._pos = 0
        self._input_fifo = list(args[:])
        self._relative_base = 0
        self._program = dict()

        if isinstance(program, str):
            program = [int(_) for _ in program.strip().split(',')]
        for index, value in enumerate(program):
            self._program[index] = value

    def _get_value(self, pos):
        return self._program[pos] if pos in self._program else 0

    def _run(self):
        output = None

        while output is None:
            op = self._get_value(self._pos) % 100
            modes = f'{self._get_value(self._pos) // 100:03d}'[::-1]

            if op == 99:
                raise HaltException()

            args = []
            args_count = 0
            dest = None
            shift = None
            skip = False

            if op in (1, 2, 7, 8):
                args_count = 2
                dest = self._get_value(self._pos + 3)
                if modes[2] == '2':
                    dest += self._relative_base
                shift = 4
            elif op == 3:
                dest = self._get_value(self._pos + 1)
                if modes[0] == '2':
                    dest += self._relative_base
                shift = 2
            elif op in (4, 9):
                args_count = 1
                shift = 2
            elif op in (5, 6):
                args_count = 2
                shift = 3

            for arg_pos in range(0, args_count):
                arg_val = self._get_value(self._pos + 1 + arg_pos)
                if modes[arg_pos] == '0':
                    args.append(self._get_value(arg_val))
                elif modes[arg_pos] == '1':
                    args.append(arg_val)
                elif modes[arg_pos] == '2':
                    args.append(self._get_value(self._relative_base + arg_val))
                else:
                    print("Invalid mode")
                    sys.exit(1)

            #print(self._program, op, args)

            if op == 1:
                self._program[dest] = args[0] + args[1]
            elif op == 2:
                self._program[dest] = args[0] * args[1]
            elif op == 3:
                if self._input_fifo:
                    self._program[dest] = self._input_fifo.pop(0)
                else:
                    raise NoInputException()
            elif op == 4:
                output = args[0]
            elif op == 5:
                if args[0]:
                    self._pos = args[1]
                    skip = True
            elif op == 6:
                if not args[0]:
                    self._pos = args[1]
                    skip = True
            elif op == 7:
                self._program[dest] = 1 if args[0] < args[1] else 0
            elif op == 8:
                self._program[dest] = 1 if args[0] == args[1] else 0
            elif op == 9:
                self._relative_base += args[0]
            else:
                print("Invalid op")
                sys.exit(1)

            if not skip:
                self._pos += shift

        return output

    def get_output(self, *args):
        self._input_fifo.extend(args)
        return self._run()


icc = ICC(next(sys.stdin))
screen = dict()

try:
    while True:
        x = icc.get_output()
        y = icc.get_output()
        tile = icc.get_output()

        screen[(x, y)] = tile
except HaltException:
    pass

count = 0
for tile in screen.values():
    if tile == 2:
        count += 1

print(count)
