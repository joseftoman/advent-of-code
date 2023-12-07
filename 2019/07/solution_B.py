#!/usr/bin/env python

import itertools
import sys

class HaltException(Exception):
    pass

class NoInputException(Exception):
    pass

class ICC():
    def __init__(self, program, phase_setting):
        self._pos = 0
        self._program = program[:]
        self._input_fifo = [phase_setting]

    def _run(self):
        output = None

        while output is None:
            op = self._program[self._pos] % 100
            modes = f'{self._program[self._pos] // 100:03d}'[::-1]

            if op == 99:
                raise HaltException()

            args = []
            args_count = 0
            dest = None
            shift = None
            skip = False

            if op in (1, 2, 7, 8):
                args_count = 2
                dest = self._program[self._pos + 3]
                shift = 4
            elif op == 3:
                dest = self._program[self._pos + 1]
                shift = 2
            elif op == 4:
                args_count = 1
                shift = 2
            elif op in (5, 6):
                args_count = 2
                shift = 3

            for arg_pos in range(0, args_count):
                arg_val = self._program[self._pos + 1 + arg_pos]
                if modes[arg_pos] == '0':
                    args.append(self._program[arg_val])
                else:
                    args.append(arg_val)

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
            else:
                print("Invalid op")
                sys.exit(1)

            if not skip:
                self._pos += shift

        return output

    def get_output(self, *args):
        self._input_fifo.extend(args)
        return self._run()


program = [int(_) for _ in next(sys.stdin).strip().split(',')]
best = None

for p in itertools.permutations(range(5, 10)):
    final = None
    signal = 0
    amps = [ICC(program, _) for _ in p]

    try:
        while True:
            for amp in amps:
                signal = amp.get_output(signal)
            final = signal
    except HaltException:
        pass

    if best is None or final > best:
        best = final
        print('MAX:', best, p)

print(best)
