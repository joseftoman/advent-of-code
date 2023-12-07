#!/usr/bin/env python

from collections import Counter, defaultdict
import sys

template = sys.stdin.readline().rstrip()
polymer = defaultdict(int)
for i in range(len(template) - 1):
    polymer[template[i:i+2]] += 1

sys.stdin.readline()

rules = {}
for line in sys.stdin:
    left, right = line.rstrip().split(' -> ')
    rules[left] = right

for step in range(40):
    new_polymer = defaultdict(int)
    for pair, freq in polymer.items():
        new_polymer[pair[0] + rules[pair]] += freq
        new_polymer[rules[pair] + pair[1]] += freq
    polymer = new_polymer

freqs = defaultdict(int)
for pair, freq in polymer.items():
    freqs[pair[0]] += freq / 2
    freqs[pair[1]] += freq / 2

freqs[template[0]] += 0.5
freqs[template[-1]] += 0.5

print(int(max(freqs.values()) - min(freqs.values())))
