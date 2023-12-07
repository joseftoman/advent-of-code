#!/usr/bin/python3

import sys
import re

password = 'fbgdceah'

swap_pos      = re.compile('swap position (\d+) with position (\d+)')
swap_letter   = re.compile('swap letter (.) with letter (.)')
rotate_steps  = re.compile('rotate (left|right) (\d+) step')
rotate_letter = re.compile('rotate based on position of letter (.)')
reverse       = re.compile('reverse positions (\d+) through (\d+)')
move          = re.compile('move position (\d+) to position (\d+)')

# Manually compiled for 8-letter long sequence
shifts = [ 7, 7, 2, 6, 1, 5, 0, 4 ]

def rotate(s, x, left = False):
    x %= len(s)
    if x == 0: return s
    if left: x = len(s) - x
    return s[-x:] + s[:len(s) - x]

for line in reversed([ l for l in sys.stdin ]):
    m = swap_pos.match(line)
    if m:
        g = tuple(map(int, m.groups()))
        password = list(password)
        ch = password[g[0]]
        password[g[0]] = password[g[1]]
        password[g[1]] = ch
        password = ''.join(password)
        continue

    m = swap_letter.match(line)
    if m:
        g = m.groups()
        password = password.replace(g[0], '#').replace(g[1], g[0]).replace('#', g[1])
        continue

    m = rotate_steps.match(line)
    if m:
        password = rotate(password, int(m.group(2)), m.group(1) == 'right')
        continue

    m = rotate_letter.match(line)
    if m:
        ch = m.group(1)
        pos = password.find(ch)
        password = rotate(password, shifts[pos])
        continue

    m = reverse.match(line)
    if m:
        g = tuple(map(int, m.groups()))
        password = password[:g[0]] + password[g[0]:g[1]+1][::-1] + password[g[1]+1:]
        continue

    m = move.match(line)
    if m:
        g = tuple(reversed(list(map(int, m.groups()))))
        if g[0] < g[1]:
            password = password[:g[0]] + password[g[0]+1:g[1]+1] + password[g[0]] + password[g[1]+1:]
        elif g[0] > g[1]:
            password = password[:g[1]] + password[g[0]] + password[g[1]:g[0]] + password[g[0]+1:]
        continue

    print("Unknown instruction:", line)

print(password)
