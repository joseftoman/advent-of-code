#!/usr/bin/env python

from collections import defaultdict
import sys

adapters = sorted([int(_) for _ in sys.stdin])
diffs = defaultdict(int)
diffs[adapters[0]] += 1
diffs[3] += 1

for i in range(1, len(adapters)):
    diffs[adapters[i] - adapters[i-1]] += 1

print(diffs[1] * diffs[3])
