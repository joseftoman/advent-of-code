#!/usr/bin/env python

import heapq
import sys

target = 'A' * 4 + 'B' * 4 + 'C' * 4 + 'D' * 4 + '_' * 7
energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
entry = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
reverse_entry = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}


def to_state(columns, hallway, *, pop_column=None, push_column=None, clear_hallway=None, add_hallway=None):
    new_state = ''

    for char in ['A', 'B', 'C', 'D']:
        offset = 0
        new_state += columns[char]
        if char == pop_column:
            new_state = new_state[:-1]
            offset = -1
        if char == push_column:
            new_state += char
            offset = 1
        new_state += '_' * (4 - len(columns[char]) - offset)

    for i in (0, 1, 3, 5, 7, 9, 10):
        char = hallway[i]
        if i == clear_hallway:
            char = '_'
        if add_hallway is not None and add_hallway[0] == i:
            char = add_hallway[1]

        new_state += char

    return new_state


def next_states(state):
    columns = {}
    for char, col in entry.items():
        columns[char] = state[col*4:(col+1)*4].replace('_', '')

    go_in = set()
    for char, col in columns.items():
        if not col or set(list(col)) == {char}:
            go_in.add(char)

    hallway = state[16] + state[17] + '_' + state[18] + '_' + state[19] + '_' + state[20] + '_' + state[21] + state[22]

    for i in range(11):
        if hallway[i] not in go_in:
            continue

        j = 2 + entry[hallway[i]] * 2
        if not hallway[min([i, j]) + 1:max(i, j)].replace('_', ''):
            cost = energy[hallway[i]] * (abs(i - j) + (4 - len(columns[hallway[i]])))
            yield (cost, to_state(columns, hallway, push_column=hallway[i], clear_hallway=i))

    for char, col in columns.items():
        if not col or char in go_in:
            continue

        amp = col[-1]
        h_start = 2 + entry[char] * 2

        dist = 5 - len(col)
        i = h_start
        while i > 0:
            i -= 1
            if hallway[i] != '_':
                break
            dist += 1
            yield (energy[amp] * dist, to_state(columns, hallway, pop_column=char, add_hallway=(i, amp)))

            if i > 2:
                i -= 1
                dist += 1
                if reverse_entry[i] in go_in and reverse_entry[i] == amp:
                    yield (energy[amp] * (dist + 4 - len(columns[amp])), to_state(columns, hallway, pop_column=char, push_column=amp))

        dist = 5 - len(col)
        i = h_start
        while i < 10:
            i += 1
            if hallway[i] != '_':
                break
            dist += 1
            yield (energy[amp] * dist, to_state(columns, hallway, pop_column=char, add_hallway=(i, amp)))

            if i < 8:
                i += 1
                dist += 1
                if reverse_entry[i] in go_in and reverse_entry[i] == amp:
                    yield (energy[amp] * (dist + 4 - len(columns[amp])), to_state(columns, hallway, pop_column=char, push_column=amp))


sys.stdin.readline()
sys.stdin.readline()
first = sys.stdin.readline()
second = sys.stdin.readline()

state = ''.join(second[index * 2 + 3] + {0: 'D', 1: 'B', 2: 'A', 3: 'C'}[index] + {0: 'D', 1: 'C', 2: 'B', 3: 'A'}[index] + first[index * 2 + 3] for index in range(4))
state += '_' * 7

known = set()
queue = [(0, state)]

while queue:
    total_cost, state = heapq.heappop(queue)
    if state in known:
        continue
    known.add(state)

    if state == target:
        print(total_cost)
        break

    for cost, next_state in next_states(state):
        if next_state not in known:
            heapq.heappush(queue, (total_cost + cost, next_state))
