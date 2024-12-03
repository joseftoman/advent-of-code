#!/usr/bin/env python

import re
import sys

total = 0
do = True

for match in re.findall(r"(mul|do|don't)\((?:(\d{1,3}),(\d{1,3}))?\)", ''.join(sys.stdin)):
    if match[0] == 'do':
        do = True
    elif match[0] == "don't":
        do = False
    elif do:
        total += int(match[1]) * int(match[2])

print(total)
