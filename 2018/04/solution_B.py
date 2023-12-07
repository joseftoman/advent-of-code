#!/usr/bin/env python

import sys
import re

log = []
guards = {}
guard = None
sleeps_from = None
re_guard = re.compile(r' #(\d+) ')

for line in sys.stdin:
    log.append(line.strip())

log.sort()

for item in log:
    if item.find('shift') != -1:
        guard = int(re_guard.search(item).group(1))
        sleeps_from = None
    else:
        minute = int(item[15:17])
        if item.find('falls') != -1:
            sleeps_from = minute
        else:
            if guard not in guards:
                guards[guard] = [0, [0] * 60]

            guards[guard][0] += minute - sleeps_from
            for x in range(sleeps_from, minute):
                guards[guard][1][x] += 1

max = [0, None]
for guard, info in guards.items():
    for minute, count in enumerate(info[1]):
        if count > max[0]:
            max = [count, guard * minute]

print(max[1])
