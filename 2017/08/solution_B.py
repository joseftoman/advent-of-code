#!/usr/bin/python3

import sys
import re

regs = {}
max = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    m = re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (-?\d+)', line)
    g = m.groups()
    if g[0] not in regs: regs[g[0]] = 0
    if g[3] not in regs: regs[g[3]] = 0

    if g[4] == '>':
        if regs[g[3]] <= int(g[5]): continue
    elif g[4] == '<':
        if regs[g[3]] >= int(g[5]): continue
    elif g[4] == '>=':
        if regs[g[3]] < int(g[5]): continue
    elif g[4] == '<=':
        if regs[g[3]] > int(g[5]): continue
    elif g[4] == '==':
        if regs[g[3]] != int(g[5]): continue
    elif g[4] == '!=':
        if regs[g[3]] == int(g[5]): continue

    if g[1] == 'inc':
        regs[g[0]] += int(g[2])
    else:
        regs[g[0]] -= int(g[2])

    if max < regs[g[0]]: max = regs[g[0]]

print(max)
