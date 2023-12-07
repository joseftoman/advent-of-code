#!/usr/bin/env python

import math
import re
import sys

match = re.match(r'target area: x=([0-9-]+)\.\.([0-9-]+), y=([0-9-]+)\.\.([0-9-]+)', sys.stdin.readline())
target = [int(_) for _ in match.groups()]

print(int(target[2] * (target[2] + 1) / 2))
