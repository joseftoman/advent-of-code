#!/usr/bin/env python

from collections import defaultdict
import re
import sys
from pyparsing import And, Char, MatchFirst, ParseException

raw_rules = {}
rules = {}
waiting = defaultdict(set)
ready = set()

for line in sys.stdin:
    line = line.strip()
    if not line:
        break

    name, content = line.split(': ')

    if content[0] == '"':
        raw_rules[name] = (content, set())
        ready.add(name)
        continue

    need = set(filter(lambda x: x != '|', content.split()))
    raw_rules[name] = [content, need]
    for item in need:
        waiting[item].add(name)

while ready:
    name = ready.pop()
    content, need = raw_rules[name]

    if content[0] == '"':
        rules[name] = Char(content[1])
    else:
        parts = [And([rules[item] for item in part.split()]) for part in content.split(' | ')]
        if len(parts) > 1:
            rules[name] = MatchFirst(parts)
        else:
            rules[name] = parts[0]

    for item in waiting.pop(name, []):
        raw_rules[item][1].remove(name)
        if not raw_rules[item][1]:
            ready.add(item)

hits = 0
parser = rules['0']

for line in sys.stdin:
    line = line.strip()
    try:
        parser.parseString(line, parseAll=True)
        hits += 1
    except ParseException:
        pass

print(hits)
