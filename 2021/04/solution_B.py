#!/usr/bin/env python

from collections import defaultdict
import sys

drawn = set()
boards = []
numbers = defaultdict(list)

draw = [int(_) for _ in sys.stdin.readline().split(',')]
sys.stdin.readline()
board_index = 0

while True:
    board = {'win': False, 'numbers': [], 'cols': [5] * 5, 'rows': [5] * 5}
    for i in range(5):
        row = [int(_) for _ in sys.stdin.readline().split()]
        for j, num in enumerate(row):
            board['numbers'].append(num)
            numbers[num].append((board_index, i, j))

    boards.append(board)
    board_index += 1

    sep = sys.stdin.readline()
    if not sep:
        break

not_won = set(range(len(boards)))

for num in draw:
    drawn.add(num)

    for pos in numbers.get(num, []):
        board = boards[pos[0]]
        if board['win']:
            continue

        board['rows'][pos[1]] -= 1
        board['cols'][pos[2]] -= 1

        if board['rows'][pos[1]] == 0 or board['cols'][pos[2]] == 0:
            board['win'] = True
            not_won.remove(pos[0])

            if not not_won:
                score = 0
                for not_drawn in [_ for _ in board['numbers'] if _ not in drawn]:
                    score += not_drawn
                print(score * num)
                sys.exit(0)
