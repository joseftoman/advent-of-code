#!/usr/bin/env python

import sys
total = 0
answers = set()


for line in sys.stdin:
    line = line.strip()
    if not line:
        total += len(answers)
        answers = set()
        continue

    answers = answers.union(set(iter(line)))

total += len(answers)

print(total)
