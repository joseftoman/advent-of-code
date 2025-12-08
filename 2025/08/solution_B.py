#!/usr/bin/env python

from functools import reduce
import sys
from typing import cast

type Box = tuple[int, int, int]


def main() -> None:
    # mapping of boxes to circuit IDs
    boxes: dict[Box, int] = {}

    # curcuits index by their IDs
    circuits: dict[int, set[Box]] = {}

    # lengths of connections, ordered
    connections: list[tuple[Box, Box, int]] = []

    next_circuit_id = 0

    for line in sys.stdin:
        box = cast(Box, tuple(map(int, line.strip().split(','))))
        boxes[box] = next_circuit_id
        circuits[next_circuit_id] = {box}
        next_circuit_id += 1

    all_boxes = list(boxes)

    for index, box1 in enumerate(all_boxes):
        for box2 in all_boxes[index + 1:]:
            # The actual distance is a square root of the sum below, but it has no effect on the ordering.
            distance = sum((box1[_] - box2[_]) ** 2 for _ in range(len(box1)))
            connections.append((box1, box2, distance))

    del all_boxes
    connections.sort(key=lambda item: item[2])
    index = -1
    
    while len(circuits) > 1:
        index += 1
        to_enlarge = boxes[connections[index][0]]
        to_merge = boxes[connections[index][1]]

        if to_enlarge == to_merge:
            continue

        circuits[to_enlarge] |= circuits[to_merge]

        for box in circuits[to_merge]:
            boxes[box] = to_enlarge

        del circuits[to_merge]

    print(connections[index][0][0] * connections[index][1][0])


if __name__ == '__main__':
    main()
