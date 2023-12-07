#!/usr/bin/env python

import sys

subj = 7
div = 20201227
pk_card = int(sys.stdin.readline().rstrip())
pk_door = int(sys.stdin.readline().rstrip())

value = 1
loop_card = 0

while value != pk_card:
    value = (value * subj) % div
    loop_card += 1

value = 1
for _ in range(loop_card):
    value = (value * pk_door) % div

print(value)
