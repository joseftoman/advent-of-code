#!/usr/bin/python3

import sys
import re
import primesieve
import string

program = []
r = {}
pos = 0
primes = set([])
primes_limit = 0

def is_prime(x):
    global primes_limit
    if x > primes_limit:
        for p in primesieve.primes(primes_limit + 1, x + 10000):
            primes.add(p)
        primes_limit = x + 10000
    return x in primes

for line in [ l.rstrip() for l in sys.stdin ]:
    i = line.split(' ')
    program.append(i)
    for arg in (1, 2):
        if i[arg] in string.ascii_lowercase and i[arg] not in r: r[i[arg]] = 0

r['a'] = 1

def get_val(arg):
    return r[arg] if arg.isalpha() else int(arg)

while pos >= 0 and pos < len(program):
    i = program[pos]
    c = i[0]

    if c == 'set':
        r[i[1]] = get_val(i[2])
    elif c == 'sub':
        r[i[1]] -= get_val(i[2])
    elif c == 'mul':
        r[i[1]] *= get_val(i[2])
    elif c == 'jnz':
        if get_val(i[1]) != 0:
            pos += get_val(i[2])
            continue
    elif c == 'npr':
        if not is_prime(get_val(i[2])): r[i[1]] += 1

    pos += 1

print(r['h'])
