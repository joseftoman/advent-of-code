#!/usr/bin/python3

import sys
import re

program = []
state = (
    { 'pos': 0, 'r': {}, 'q': [] },
    { 'pos': 0, 'r': {}, 'q': [] },
)
out = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    i = line.split(' ')
    program.append(i)
    for arg in (0, 1):
        if i[arg].isalpha and i[arg] not in state[0]['r']:
            state[0]['r'][i[arg]] = 0
            state[1]['r'][i[arg]] = 0

state[0]['r']['p'] = 0
state[1]['r']['p'] = 1

def get_val(arg):
    return r[arg] if arg.isalpha() else int(arg)

while state[0]['pos'] >= 0 and state[0]['pos'] < len(program) and state[1]['pos'] >= 0 and state[1]['pos'] < len(program):
    deadlock = 0
    nodead = [-1, -1]

    for p in (0, 1):
        p2 = (p + 1) % 2
        s = state[p]
        r = s['r']

        while True:
            nodead[p] += 1
            i = program[s['pos']]
            c = i[0]

            if c == 'snd':
                state[p2]['q'].append(get_val(i[1]))
                if p == 1: out += 1
            elif c == 'set':
                r[i[1]] = get_val(i[2])
            elif c == 'add':
                r[i[1]] += get_val(i[2])
            elif c == 'mul':
                r[i[1]] *= get_val(i[2])
            elif c == 'mod':
                r[i[1]] %= get_val(i[2])
            elif c == 'rcv':
                if len(s['q']):
                    r[i[1]] = s['q'].pop(0)
                else:
                    if nodead[p] == 0: deadlock += 1
                    break;
            elif c == 'jgz':
                if get_val(i[1]) > 0:
                    s['pos'] += get_val(i[2])
                    continue

            s['pos'] += 1

    if deadlock == 2: break

print(out)
