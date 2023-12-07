#!/usr/bin/env python

from collections import defaultdict
import re
import sys

bags = dict()
ready = set()
parents = defaultdict(list)
regex_main = re.compile(r'(\w+ \w+) bags contain(.*)')
regex_group = re.compile(r'(\d+) (\w+ \w+) bag')

for rule in sys.stdin:
    rule = rule.strip()
    parent, contents = regex_main.fullmatch(rule).groups()
    if contents[:3] == ' no':
        bags[parent] = {'children': {}, 'left': 0, 'size': 0}
        ready.add(parent)
        continue

    children = {}
    for item in contents.split(','):
        (amount, child) = regex_group.search(item).groups()
        parents[child].append(parent)
        children[child] = int(amount)
    bags[parent] = {'children': children, 'left': len(children), 'size': 0}

while ready:
    name = ready.pop()
    #print(f'\nREADY {name}:')
    for child, amount in bags[name]['children'].items():
        bags[name]['size'] += amount * (bags[child]['size'] + 1)
        #print(f'- CHILD {child}: {amount} * ({bags[child]["size"]} + 1) = {amount * (bags[child]["size"] + 1)}')
    #print(f'- TOTAL = {bags[name]["size"]}')

    for parent in parents[name]:
        bags[parent]['left'] -= 1
        #print(f'- PARENT {parent}: {bags[parent]["left"]}')
        if bags[parent]['left'] == 0:
            ready.add(parent)

print(bags['shiny gold']['size'])
