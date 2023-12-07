#!/usr/bin/python3

# Hackish solution!
# True solution would require something like distance matrix.
# The simulation would continue while there is a pair of particles which distance is decreasing.

import sys

particles = []

for line in [ l.rstrip() for l in sys.stdin ]:
    vectors = line.split(', ')
    p = []
    for v in vectors:
        p.append([ int(x) for x in v[3:-1].split(',') ])
    particles.append(p)

while True:
    groups = {}
    i = 0

    for p in particles:
        for j in range(0, 3):
            p[1][j] += p[2][j]
            p[0][j] += p[1][j]

        pos = tuple(p[0])
        if pos not in groups:
            groups[pos] = []
        groups[pos].append(i)
        i += 1

    new_particles = []

    for s in groups.values():
        if len(s) == 1:
            new_particles.append(particles[s[0]])

    particles = new_particles
    print(len(particles))
