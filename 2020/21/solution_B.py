#!/usr/bin/env python

from collections import defaultdict
import re
import sys

allergens = {}
ingredients = defaultdict(set)
freqs = defaultdict(int)
regex = re.compile(r'(.*) \(contains (.*)\)')
ready = set()

for line in sys.stdin:
    m = regex.match(line)
    ingr = m.group(1).split()
    alle = m.group(2).split(', ')

    for i in ingr:
        freqs[i] += 1
        for a in alle:
            ingredients[i].add(a)

    for a in alle:
        if a not in allergens:
            allergens[a] = set(ingr)
        else:
            for i in ingr:
                if i not in allergens[a]:
                    ingredients[i].remove(a)
            for i in allergens[a]:
                if i not in ingr:
                    ingredients[i].remove(a)
            allergens[a] &= set(ingr)

        if len(allergens[a]) == 1:
            ready.add(a)

result = []
sort = {}
while ready:
    a = ready.pop()
    i = allergens[a].pop()
    sort[i] = a
    result.append(i)

    for key, value in allergens.items():
        value.discard(i)
        if len(value) == 1:
            ready.add(key)

result.sort(key=lambda i: sort[i])
print(','.join(result))
