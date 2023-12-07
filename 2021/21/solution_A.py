#!/usr/bin/env python

import sys

throws = 0

def die_generator():
    global throws
    value = 1

    while True:
        throws += 1
        yield value
        value += 1
        if value > 100:
            value = 1

player = 0
players = [int(line.strip()[-1]) for line in sys.stdin]
scores = [0, 0]
die = die_generator()

while max(scores) < 1000:
    move = next(die) + next(die) + next(die)
    players[player] = ((players[player] - 1 + move) % 10) + 1
    scores[player] += players[player]
    player = (player + 1) % 2

print(min(scores) * throws)
