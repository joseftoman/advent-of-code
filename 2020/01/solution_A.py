#!/usr/bin/env python

import sys
options = set()

for num in [int(_) for _ in sys.stdin]:
    if num in options:
        print(num * (2020 - num))
        break
    options.add(2020 - num)
