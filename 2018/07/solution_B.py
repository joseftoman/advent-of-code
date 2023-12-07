#!/usr/bin/env python

import sys

steps = {}
step_duration = 60
idle = 5
busy = []
progress = 0

for line in sys.stdin:
    step_one = line[5]
    step_two = line[36]

    for step in (step_one, step_two):
        if step not in steps: steps[step] = set()

    steps[step_two].add(step_one)

while steps or busy:
    finished = set()

    if busy:
        new_busy = []
        progress = min([worker[0] for worker in busy])

        for worker in busy:
            if worker[0] == progress:
                finished.add(worker[1])
                idle += 1
            else:
                new_busy.append(worker)

        busy = new_busy
    
    ready = []

    for name, needs in steps.items():
        for step in finished:
            needs.discard(step)
        if not len(needs):
            ready.append(name)

    ready.sort(key=lambda char: ord('Z') - ord(char))

    while ready and idle:
        step = ready.pop()
        idle -= 1
        busy.append((progress + step_duration + ord(step) - ord('A') + 1, step))
        del steps[step]

print(progress)
