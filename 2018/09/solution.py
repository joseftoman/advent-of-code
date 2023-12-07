#!/usr/bin/env python

import sys

if len(sys.argv) == 3:
    (players, marbles) = [int(x) for x in sys.argv[1:]]
else:
    print(f'usage: {sys.argv[0]} PLAYERS LAST_MARBLE')
    sys.exit(1)

circle = {0: [0, 0]}
marble = 0
current = 0
player = -1

score = [0] * players
max_score = 0

while marble < marbles:
    marble += 1
    player = (player + 1) % players

    if marble % 23:
        left = circle[current][1]
        right = circle[left][1]
        circle[marble] = [left, right]
        circle[left][1] = marble
        circle[right][0] = marble
        current = marble
    else:
        for _ in range(0, 7):
            current = circle[current][0]
        left = circle[current][0]
        right = circle[current][1]
        circle[left][1] = right
        circle[right][0] = left
        del circle[current]
        score[player] += marble + current
        current = right

        if score[player] > max_score:
            max_score = score[player]

print(max_score)
