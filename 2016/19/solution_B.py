#!/usr/bin/python3

size = 3018458
elves = list(range(1, size + 1))

while len(elves) > 1:
    L = len(elves)
    C = int(L / 2)
    new_elves = []

    if L % 2 == 0:
        if L % 3 == 0:
            new_elves = elves[2::3]
        elif L % 3 == 1:
            new_elves = elves[:C:3]
            new_elves.append(elves[C-1])
            new_elves += elves[C+2::3]
        else:
            new_elves = elves[1:C:3]
            new_elves.append(elves[C-1])
            new_elves += elves[C+2::3]
    else:
        if L % 3 == 0:
            new_elves = elves[2::3]
        elif L % 3 == 1:
            new_elves = elves[:C:3]
            new_elves.append(elves[C-1])
            new_elves += elves[C+1::3]
        else:
            new_elves = elves[1:C:3]
            new_elves += elves[C+1::3]

    elves = new_elves

print(elves[0])
