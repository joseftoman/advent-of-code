#!/usr/bin/python3

import string
import sys
import re

def perm_deg(p):
    tmp = list(range(0, dancers))
    orig = tmp[:]
    deg = 0

    while True:
        deg += 1
        next_tmp = []
        for i in range(0, dancers):
            next_tmp.append(tmp[p[i]])

        tmp = next_tmp
        if tmp == orig: return(deg)

dancers = 16
steps = int(1e9)
positions = list(range(0, dancers))
letters = list(range(0, dancers))
a_shift = ord('a')

for move in sys.stdin.readline().rstrip().split(','):
    m = re.match(r's(\d+)$', move)
    if m:
        num = int(m.group(1))
        positions = positions[-num:] + positions[:-num]
        continue
    
    m = re.match(r'x(\d+)/(\d+)$', move)
    if m:
        pos = [ int(x) for x in m.groups() ]
        tmp = positions[pos[0]]
        positions[pos[0]] = positions[pos[1]]
        positions[pos[1]] = tmp
        continue

    m = re.match(r'p(\w)/(\w)$', move)
    if m:
        for i in range(0, dancers):
            if chr(letters[i] + a_shift) == m.group(1):
                letters[i] = ord(m.group(2)) - a_shift
            elif chr(letters[i] + a_shift) == m.group(2):
                letters[i] = ord(m.group(1)) - a_shift

p_deg = perm_deg(positions)
l_deg = perm_deg(letters)

progs = list(string.ascii_lowercase[:dancers]) 

for i in range(0, steps % p_deg):
    next_progs = []
    for i in range(0, dancers):
        next_progs.append(progs[positions[i]])
    progs = next_progs

for i in range(0, steps % l_deg):
    next_progs = []
    for i in range(0, dancers):
        next_progs.append(chr(letters[ord(progs[i]) - a_shift] + a_shift))
    progs = next_progs

print(''.join(progs))
