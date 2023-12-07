#!/usr/bin/env python

from collections import defaultdict
import re
import sys

parents = defaultdict(list)
regex_main = re.compile(r'(\w+ \w+) bags contain(.*)')
regex_group = re.compile(r'\d+ (\w+ \w+) bag')

for rule in sys.stdin:
    rule = rule.strip()
    parent, contents = regex_main.fullmatch(rule).groups()
    if contents[:3] == ' no':
        continue

    for item in contents.split(','):
        child = regex_group.search(item).group(1)
        parents[child].append(parent)

task = set(['shiny gold'])
seen = set()
total = 0

while task:
    name = task.pop()
    seen.add(name)
    for item in parents[name]:
        if item not in seen and item not in task:
            total += 1
            task.add(item)

print(total)
