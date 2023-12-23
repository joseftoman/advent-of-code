#!/usr/bin/env python

from collections import defaultdict, deque
import sys


def walk(graph, node, visited, current_dist, end):
    if node == end:
        return current_dist

    best = 0
    for next_node, node_dist in graph[node]:
        if next_node in visited:
            continue
        dist = walk(graph, next_node, visited | {node}, current_dist + node_dist, end)
        if dist > best:
            best = dist

    return best


def create_graph(grid, start, end):
    visited = set()
    graph = defaultdict(list)
    nodes = {start}
    queue = deque([(start, (1, 0))])

    while queue:
        node, diff = queue.popleft()
        dist = 0
        pos = (node[0] + diff[0], node[1] + diff[1])
        if pos in visited:
            continue

        pos = node
        options = [diff]

        while len(options) == 1:
            pos = (pos[0] + options[0][0], pos[1] + options[0][1])
            dist += 1
            visited.add(pos)
            options = []

            if pos == end:
                options = []
                graph[node].append((pos, dist))
                break

            for diff in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_pos = (pos[0] + diff[0], pos[1] + diff[1])
                if new_pos in nodes:
                    if new_pos != node:
                        graph[node].append((new_pos, dist + 1))
                        graph[new_pos].append((node, dist + 1))
                    continue
                if grid[new_pos] == '#' or new_pos in visited:
                    continue

                options.append(diff)

        if not options:
            continue

        nodes.add(pos)
        graph[node].append((pos, dist))
        graph[pos].append((node, dist))
        for diff in options:
            queue.append((pos, diff))

    return graph


def main():
    grid = {}

    for y, line in enumerate(sys.stdin):
        end = (y, len(line.strip()) - 2)
        for x, char in enumerate(line.strip()):
            grid[(y, x)] = char

    graph = create_graph(grid, (0, 1), end)
    print(walk(graph, (0, 1), {(0, 1)}, 0, end))


if __name__ == '__main__':
    main()
