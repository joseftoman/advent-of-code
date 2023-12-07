#!/usr/bin/env python

import sys

line = next(sys.stdin).strip()
for index in range(14, len(line)):
    if len(set(line[index-14:index])) == 14:
        print(index)
        break
