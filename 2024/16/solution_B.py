#!/usr/bin/env python

import heapq
import sys

MOVES = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
MOVE_TO_FACING = {val: key for key, val in MOVES.items()}
ROTATIONS = {
    'N': {'E': 1000, 'S': 2000, 'W': 1000},
    'E': {'S': 1000, 'W': 2000, 'N': 1000},
    'S': {'E': 1000, 'N': 2000, 'W': 1000},
    'W': {'N': 1000, 'E': 2000, 'S': 1000},
}


def main():
    maze = {}
    visited = {}  # (y, x, facing) -> (minimum points, set of directly preceeing tiles on best paths)
    heap = []
    target = None
    threshold = None
    trace_back = set()

    for y, line in enumerate(sys.stdin):
        for x, char in enumerate(line.strip()):
            maze[(y, x)] = char
            if char == 'S':
                heap = [(0, (y, x), 'E', None)]
            if char == 'E':
                target = (y, x)

    # Find all best paths
    while heap:
        points, pos, facing, prev_tile = heapq.heappop(heap)

        if threshold is not None and points > threshold:
            # We have found all best paths
            break

        if pos == target:
            # We have reached the End Tile. Let's continue looking for other paths with the same score.
            threshold = points
            trace_back.add((prev_tile, facing))
            continue

        for diff in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y = pos[0] + diff[0]
            x = pos[1] + diff[1]
            new_facing = MOVE_TO_FACING[diff]
            if maze[(y, x)] == '#':
                continue

            facing_price = ROTATIONS[facing].get(new_facing, 0)
            if facing_price == 2000:
                # There's no point in turning back
                continue

            marker = (*pos, new_facing)
            if marker not in visited:
                visited[marker] = (points + facing_price, set() if not prev_tile else {prev_tile})
            else:
                # We've already been there.
                if visited[marker][0] == points + facing_price:
                    # If the score is the same, let's save it for the final trace back.
                    visited[marker][1].add(prev_tile)
                # Either way, there's no point in going forward.
                continue

            heapq.heappush(heap, (points + facing_price + 1, (y, x), new_facing, pos))

    # Trace our steps back to find all tiles on best paths
    best_tiles = {target}
    while trace_back:
        tile, facing = trace_back.pop()
        best_tiles.add(tile)

        marker = (*tile, facing)
        if marker not in visited:
            continue
        for prev_tile in visited[marker][1]:
            best_tiles.add(prev_tile)
            diff = (tile[0] - prev_tile[0], tile[1] - prev_tile[1])
            trace_back.add((prev_tile, MOVE_TO_FACING[diff]))
        visited.pop(marker)

    print(len(best_tiles))


if __name__ == '__main__':
    main()
