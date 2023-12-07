#!/usr/bin/env python

import sys

fs_size = 70000000
target_free = 30000000
fs = {}
path = []
result = 0

for line in sys.stdin:
    tokens = line.strip().split()

    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '..':
                path.pop()
            else:
                if tokens[2] == '/':
                    path = ['/']
                else:
                    path.append(tokens[2])

                if tuple(path) not in fs:
                    fs[tuple(path)] = {'size': 0, 'dirs': set()}

    else:
        if tokens[0] == 'dir':
            fs[tuple(path)]['dirs'].add(tuple(path + [tokens[1]]))
        else:
            fs[tuple(path)]['size'] += int(tokens[0])


def walk(path):
    global fs
    global result

    for child in fs[path]['dirs']:
        walk(child)
        fs[path]['size'] += fs[child]['size']

    if fs[path]['size'] <= 100000:
        result += fs[path]['size']


walk(('/',))

threshold = target_free - (fs_size - fs[('/',)]['size'])
best = None
for item in fs.values():
    if item['size'] >= threshold and (best is None or item['size'] < best):
        best = item['size']

print(best)
