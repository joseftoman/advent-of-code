#!/usr/bin/env python

from collections import deque
import sys

def score(d):
    mult = 1
    total = 0

    while d:
        total += d.pop() * mult
        mult += 1

    return total

def play_game(d1, d2, get_score=False):
    one = deque(d1)
    two = deque(d2)
    states = set()

    while one and two:
        state = (tuple(one), tuple(two))
        if state in states:
            two = False
            break
        states.add(state)

        c1 = one.popleft()
        c2 = two.popleft()

        if c1 <= len(one) and c2 <= len(two):
            one_wins = play_game(list(one)[:c1], list(two)[:c2])
        else:
            one_wins = c1 > c2

        if one_wins:
            one.extend([c1, c2])
        else:
            two.extend([c2, c1])

    if get_score:
        return score(one) if one else score(two)
    return bool(one)


d1 = []
d2 = []

sys.stdin.readline()
for line in sys.stdin:
    if not line.strip():
        break
    d1.append(int(line))

sys.stdin.readline()
for line in sys.stdin:
    d2.append(int(line))

print(play_game(d1, d2, True))
