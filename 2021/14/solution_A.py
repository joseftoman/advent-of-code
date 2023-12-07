#!/usr/bin/env python

from collections import Counter
import sys

polymer = sys.stdin.readline().rstrip()
sys.stdin.readline()

rules = {}
for line in sys.stdin:
    left, right = line.rstrip().split(' -> ')
    rules[left] = right

for _ in range(10):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i] + rules[polymer[i:i+2]]
    new_polymer += polymer[-1]
    polymer = new_polymer

freqs = Counter(list(new_polymer))
print(max(freqs.values()) - min(freqs.values()))
