#!/usr/bin/env python

import sys
total = 0
answers = None


for line in sys.stdin:
    line = line.strip()
    if not line:
        total += len(answers)
        answers = None
        continue

    current_set = set(iter(line))
    if answers is None:
        answers = current_set
    else:
        answers = answers.intersection(current_set)

total += len(answers)

print(total)
