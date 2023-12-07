#!/usr/bin/env python

import sys
steps = {}
order = ''

for line in sys.stdin:
    step_one = line[5]
    step_two = line[36]

    for step in (step_one, step_two):
        if step not in steps: steps[step] = set()

    steps[step_two].add(step_one)

while steps:
    best = 'Z'

    for name, needs in steps.items():
        if order:
            needs.discard(order[-1])
        if not len(needs) and name < best:
            best = name

    order += best
    del steps[best]

print(order)
