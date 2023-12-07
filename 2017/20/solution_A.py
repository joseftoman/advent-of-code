#!/usr/bin/python3

import sys

slowest = None
i = 0

for line in [ l.rstrip() for l in sys.stdin ]:
    parts = [ [ abs(int(x)) for x in p[3:-1].split(',') ] for p in line.split(', ') ]

    constant = 0
    acceleration = 0
    distance = sum(parts[0])
    for j in range(0, 3):
        if parts[2][j] == 0:
            constant += parts[1][j]
        else:
            acceleration += parts[2][j]

    if (slowest is None
        or (acceleration < slowest[1]
            or ((acceleration == slowest[1] and constant < slowest[2])
                or (acceleration == slowest[1] and constant == slowest[2] and distance < slowest[3])
            )
        )
    ):
        slowest = [ i, acceleration, constant, distance ]

    i += 1

print(slowest[0])
