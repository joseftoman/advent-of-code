#!/usr/bin/env python

import sys

line = next(sys.stdin).strip()
for index in range(4, len(line)):
    if len(set(line[index-4:index])) == 4:
        print(index)
        break
