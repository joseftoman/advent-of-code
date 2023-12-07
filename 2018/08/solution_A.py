#!/usr/bin/env python

import sys

tree = [int(x) for x in sys.stdin.readline().split(None)]
tree.reverse()

def walk_tree():
    children = tree.pop()
    meta = tree.pop()
    meta_sum = 0

    for _ in range(0, children):
        meta_sum += walk_tree()

    for _ in range(0, meta):
        meta_sum += tree.pop()

    return meta_sum

print(walk_tree())
