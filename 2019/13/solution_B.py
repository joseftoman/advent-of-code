#!/usr/bin/env python

import sys
from time import sleep

#from pynput import keyboard
#from rich.console import Console

#console = Console()
screen = {}
score = 0
max_x = 0
max_y = 0

#def read_key():
#    move = 0
#
#    def on_press(key):
#        nonlocal move
#        if isinstance(key, keyboard.Key):
#            if key == keyboard.Key.left:
#                move = -1
#            elif key == keyboard.Key.right:
#                move = 1
#
#        return False
#
#    with keyboard.Listener(on_press=on_press, suppress=True) as listener:
#        listener.join()
#
#    return move

def render(screen, icc):
    out = ''
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) not in screen or screen[(x, y)] == 0:
                out += ' '
            else:
                out += {1: '[yellow]#[/]', 2: '[blue]x[/]', 3: '[white]T[/]', 4: '[red]o[/]'}[screen[(x, y)]]
                if screen[(x, y)] == 4:
                    ball_pos = x
                if screen[(x, y)] == 3:
                    paddle_pos = x


        out += '\n'

    out += f'\nSCORE = {score}\n'

    if not icc._input_fifo:
        if ball_pos < paddle_pos:
            icc.set_input(-1)
        else:
            icc.set_input(1)

    console.clear()
    console.print(out)
    sleep(0.05)

def move_paddle(screen, icc):
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in screen:
                if screen[(x, y)] == 4:
                    ball_pos = x
                if screen[(x, y)] == 3:
                    paddle_pos = x

    if not icc._input_fifo:
        if ball_pos < paddle_pos:
            icc.set_input(-1)
        else:
            icc.set_input(1)

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
                #render(screen, self)
                move_paddle(screen, self)
                if self._input_fifo:
                    self._program[dest] = self._input_fifo.pop(0)
                else:
                    raise NoInputException()
                #    self._program[dest] = read_key()
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
    global max_x, max_y, score
    icc = ICC(next(sys.stdin), -1, 0)
    #console.clear()

    try:
        while True:
            x = icc.get_output()
            y = icc.get_output()
            if x == -1 and y == 0:
                new_score = icc.get_output()
                if new_score > 0:
                    score = new_score
                continue

            tile = icc.get_output()

            screen[(x, y)] = tile
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    except HaltException:
        print(score)

    #console.print('SCORE =', score)
    #read_key()

if __name__ == '__main__':
    main()
