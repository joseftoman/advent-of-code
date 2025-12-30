#!/usr/bin/env python

import sys

type Room = tuple[int, int]


def follow_directions(heads: set[Room], directions: str, pos: int, rooms: set[Room], doors: set[tuple[Room, Room]]) -> tuple[int, set[Room]]:
    initial_heads = heads.copy()
    final_heads: set[Room] = set()

    while pos < len(directions):
        match directions[pos]:
            case '(':
                #print(f'Opening new layer of nesting')
                pos, heads = follow_directions(heads, directions, pos + 1, rooms, doors)
                #print(f'Nesting finished -> {pos}, {heads}')
            case '|':
                #print(f'New branch. Finalize {heads}. Loading {initial_heads}')
                final_heads |= heads
                heads = initial_heads.copy()
            case ')':
                #print(f'Closing current layer of nesting, finalize {heads}')
                final_heads |= heads
                return pos, final_heads
            case 'N' | 'E' | 'S' | 'W':
                diff = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}[directions[pos]]
                next_heads: set[Room] = set()

                for head in heads:
                    next_head = (head[0] + diff[0], head[1] + diff[1])
                    next_heads.add(next_head)
                    rooms.add(next_head)
                    doors.add((head, next_head))
                    doors.add((next_head, head))

                #print(f'Simple step: {directions[pos]}={diff}, {heads} -> {next_heads}')
                heads = next_heads

        pos += 1

    return pos, final_heads | heads


def find_paths(first_room: Room, rooms: set[Room], doors: set[tuple[Room, Room]]) -> dict[Room, int]:
    distances: dict[Room, int] = {first_room: 0}
    remaining_rooms: set[Room] = rooms - {first_room}
    current_rooms: set[Room] = {first_room}
    distance = 0

    while remaining_rooms:
        distance += 1
        next_rooms: set[Room] = set()

        for room in current_rooms:
            for diff in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_room = (room[0] + diff[0], room[1] + diff[1])
                if next_room in remaining_rooms and (room, next_room) in doors:
                    distances[next_room] = distance
                    next_rooms.add(next_room)
                    remaining_rooms.remove(next_room)

        current_rooms = next_rooms

    return distances


def main() -> None:
    directions = next(sys.stdin).strip()
    first_room = (0, 0)
    rooms: set[Room] = set([first_room])
    doors: set[tuple[Room, Room]] = set()

    follow_directions({first_room}, directions[1:-1], 0, rooms, doors)

    distances = find_paths(first_room, rooms, doors)
    print(max(distances.values()))



if __name__ == '__main__':
    main()
