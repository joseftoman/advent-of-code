#!/usr/bin/python3

import sys
import itertools

max_floor = 3
known = dict()
queue = []

elements = sys.stdin.readline().rstrip()
floors = [ line.rstrip() for line in sys.stdin ]
size = len(elements)
elem_map = {}
for i in range(size): elem_map[elements[i]] = i
target = str(max_floor)+'::::'+elements.upper()+elements

def check_floor(floor):
    has_generator = sum([ int(ch) for ch in floor[0:size] ])
    for i in range(size, size * 2):
        if floor[i] == '1' and floor[i - size] == '0' and has_generator: return 0
    return 1

def compress_floor(floor):
    state = ''
    for i in range(0, size * 2):
        if floor[i] == '0': continue
        if i < size:
            state += elements[i].upper()
        else:
            state += elements[i-size]
    return state

def compress(pos, floors):
    state = str(pos);
    for f in floors:
        state += ':'+compress_floor(f)
    return state

def decompress(state):
    parts = state.split(':')
    floors = []

    for f in parts[1:]:
        items = set(f)
        g = ''
        m = ''
        for ch in elements:
            g += '1' if ch.upper() in items else '0'
            m += '1' if ch in items else '0'
        floors.append(g+m)

    return (int(parts[0]), floors)

def alter_floor(floor, items, add):
    floor = list(floor)

    for item in items:
        pos = 0 if item.isupper() else size
        pos += elem_map[item.lower()]
        floor[pos] = '1' if add else '0'

    return ''.join(floor)

def alter_floors(floors, pos, items):
    new_floor = alter_floor(floors[pos], items, True);
    if check_floor(new_floor):
        new_floors = floors[:]
        new_floors[pos] = new_floor
        return new_floors
    else:
        return None

def get_next_with_load(pos, floors, items):
    next = []
    directions = [1]
    # When going down we always bring only a single chip.
    if len(items) == 1 and items[0].islower: directions.append(-1)

    cur_floor = alter_floor(floors[pos], items, False)
    if not check_floor(cur_floor): return None

    for dir in directions:
        new_pos = pos + dir
        if new_pos < 0 or new_pos > max_floor: continue

        new_floors = alter_floors(floors, new_pos, items)
        if new_floors is not None:
            new_floors[pos] = cur_floor
            next.append(compress(new_pos, new_floors))

    return next

def get_next(pos, floors):
    next = []
    items = compress_floor(floors[pos])

    for pair in itertools.combinations(items, 2):
        n = get_next_with_load(pos, floors, list(pair))
        if n is not None: next += n

    for item in items:
        n = get_next_with_load(pos, floors, [item])
        if n is not None: next += n

    return next

state = compress(0, floors)
queue.append(state)
known[state] = 0

while queue:
    state = queue.pop(0)
    if state in known and known[state] > 0: continue
    [ level, floors ] = decompress(state)

    for next in get_next(level, floors):
        if next in known: continue
        if next == target:
            print(-known[state] + 1)
            queue = []
            break
        queue.append(next)
        known[next] = known[state] - 1

    known[state] *= -1
