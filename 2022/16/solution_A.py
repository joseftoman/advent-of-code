#!/usr/bin/env python

from collections import defaultdict
import heapq
import sys


def test_known(known, valves, pos, time, released):
    descr = (''.join(sorted(valves)), pos)
    if descr not in known:
        return True

    prev_time, prev_released, prev_flow = known[descr]
    return prev_released + (time - prev_time) * prev_flow > released


# state = (time, pressure released, flow rate, opportunity, tie breaker, position, open valves)
def main():
    max_time = 30
    flows = {}
    edges = defaultdict(dict)
    read = 0
    queue = []
    tie_breaker = 0
    known = {}
    best = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            read += 1
            continue

        tokens = line.split()

        if read == 0:
            flows[tokens[0]] = int(tokens[1]) * -1
        elif read == 1:
            edges[tokens[0]][tokens[1]] = int(tokens[2])
            edges[tokens[1]][tokens[0]] = int(tokens[2])
        else:
            heapq.heappush(queue, (int(tokens[1]), 0, 0, flows[tokens[0]], tie_breaker, tokens[0], set()))
            tie_breaker += 1

    while queue:
        #time, released, flow, _, _, pos, valves = heapq.heappop(queue)
        state = heapq.heappop(queue)
        print('\nState entered:', state)
        time, released, flow, _, _, pos, valves = state
        valves_str = ''.join(sorted(valves))
        descr = (valves_str, pos)
        if not test_known(known, valves, pos, time, released):
            print('- known')
            continue
        known[descr] = (time, released, flow)

        projection = released + flow * (max_time - time)
        if projection < best:
            best = projection
            print('- new best:', -projection)

        if time == max_time:
            print("- time's up")
            continue

        if len(valves) == len(flows):
            print('- all open')
            continue

        if pos not in valves:
            descr = (''.join(sorted(valves | {pos})), pos)
            if test_known(known, valves | {pos}, pos, time + 1, released + flow):
                # open new valve
                heapq.heappush(queue, (time + 1, released + flow, flow + flows[pos], 0, tie_breaker, pos, valves | {pos}))
                print(f'- open valve T{tie_breaker}')
                tie_breaker += 1

        for dest in edges[pos]:
            new_time = time + edges[pos][dest]
            new_released = released + edges[pos][dest] * flow
            if not test_known(known, valves, dest, new_time, new_released) or new_time > max_time:
                continue
            heapq.heappush(queue, (new_time, new_released, flow, 0 if dest in valves else flows[dest], tie_breaker, dest, valves))
            print('- go to', dest, f'T{tie_breaker}')
            tie_breaker += 1

    print(-best)


if __name__ == '__main__':
    main()
