#!/usr/bin/env python

import functools
import sys

players = [int(line.strip()[-1]) for line in sys.stdin]
wins = [0, 0]

# All multiverse versions for a sequence of 3 die rolls (3 * 3 * 3 = 27)
# To speed things up a bit
options = [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]

@functools.lru_cache(maxsize=None)
def play(space1, space2, score1, score2, player, move):
    wins = [0, 0]
    spaces = [space1, space2]
    scores = [score1, score2]

    spaces[player] = ((spaces[player] - 1 + move) % 10) + 1
    scores[player] += spaces[player]

    if max(scores) >= 21:
        if scores[0] > scores[1]:
            wins[0] += 1
        else:
            wins[1] += 1
        return wins

    player = (player + 1) % 2
    for move in options:
        w = play(*spaces, *scores, player, move)
        wins[0] += w[0]
        wins[1] += w[1]

    return wins

for move in options:
    w = play(*players, 0, 0, 0, move)
    wins[0] += w[0]
    wins[1] += w[1]

print(max(wins))
