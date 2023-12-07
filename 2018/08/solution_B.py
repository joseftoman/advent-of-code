#!/usr/bin/env python

import sys

tree = [int(x) for x in sys.stdin.readline().split(None)]
tree.reverse()

def walk_tree():
    children = tree.pop()
    meta = tree.pop()
    node_value = 0

    node_values = [walk_tree() for _ in range(0, children)]

    for _ in range(0, meta):
        meta = tree.pop()
        if children:
            if meta <= len(node_values) and meta > 0:
                node_value += node_values[meta - 1]
        else:
            node_value += meta

    return node_value

print(walk_tree())
