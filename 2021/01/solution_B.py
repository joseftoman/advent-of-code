#!/usr/bin/env python

from collections import deque
import sys

prev = None
history = deque()
inc = 0

for num in [int(_) for _ in sys.stdin]:
    drop = None
    if len(history) == 3:
        drop = history.popleft()

    current = (prev or 0) + num - (drop or 0)
    history.append(num)
    if len(history) < 3:
        continue

    if prev is not None and prev < current:
        inc += 1
    prev = current

print(inc)
