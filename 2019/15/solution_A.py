#!/usr/bin/env python

import sys
from time import sleep

from rich.console import Console

def get_new_position(pos, move):
    x, y = pos

    if move == 1:
        y -= 1
    elif move == 2:
        y += 1
    elif move == 3:
        x -= 1
    else:
        x += 1

    return x, y


def go_back(pos, track, icc):
    move = track.pop()
    move = {1: 2, 2: 1, 3: 4, 4: 3}[move]
    icc.get_output(move)
    return get_new_position(pos, move)


def render(console, plan, pos, edge):
    console.clear()

    blank = console.size.height // 2 + edge[1]
    console.line(blank)

    offset = console.size.width // 2 + edge[0]
    offset = ' ' * offset

    for y in range(edge[1], edge[3] + 1):
        line = offset

        for x in range(edge[0], edge[2] + 1):
            if (x, y) in plan:
                tile = plan[(x, y)]
                if x == pos[0] and y == pos[1]:
                    line += '[blue]D[/]' if tile == 'O' else '[white]D[/]'
                else:
                    color = {'.': 'grey', '#': 'yellow', 'O': 'blue'}[tile]
                    line += f'[{color}]{tile}[/]'
            else:
                line += ' '

        console.print(line)


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

    def set_input(self, *args):
        self._input_fifo.extend(args)

    def get_output(self, *args):
        self._input_fifo.extend(args)
        return self._run()


def main():
    console = Console()
    pos = (0, 0)
    edge = [0, 0, 0, 0]
    plan = {pos: '.'}
    track = []
    icc = ICC(next(sys.stdin))

    try:
        while True:
            if False:
                render(console, plan, pos, edge)
                sleep(0.1)

            move = None
            for direction in (1, 2, 3, 4):
                new_pos = get_new_position(pos, direction)
                if new_pos not in plan:
                    move = direction
                    break

            if move is None:
                if not track:
                    break
                pos = go_back(pos, track, icc)
                continue

            result = icc.get_output(move)
            if not result:
                plan[new_pos] = '#'
            else:
                plan[new_pos] = '.' if result == 1 else 'O'
                pos = new_pos
                track.append(move)

            for i in [0, 1]:
                if new_pos[i] < edge[i]:
                    edge[i] = new_pos[i]
                if new_pos[i] > edge[i + 2]:
                    edge[i + 2] = new_pos[i]


    except HaltException:
        pass

    render(console, plan, pos, edge)


if __name__ == '__main__':
    main()
