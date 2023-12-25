#!/usr/bin/env python

import math
import sys

import networkx as nx


def main():
    graph = nx.Graph()

    for line in sys.stdin:
        left, right = line.strip().split(':')
        if left not in graph.nodes:
            graph.add_node(left)

        for node in right.split():
            if node not in graph.nodes:
                graph.add_node(node)
            graph.add_edge(left, node)

    cut = nx.minimum_edge_cut(graph)
    assert len(cut) == 3

    for edge in cut:
        graph.remove_edge(*edge)

    print(math.prod(map(len, nx.connected_components(graph))))


if __name__ == '__main__':
    main()
