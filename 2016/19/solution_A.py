#!/usr/bin/python3

size = 3018458
elves = list(range(1, size + 1))

while len(elves) > 1:
    new_elves = elves[::2]
    if len(elves) % 2 == 1: new_elves = new_elves[1:]
    elves = new_elves

print(elves[0])
