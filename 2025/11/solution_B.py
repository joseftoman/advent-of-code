#!/usr/bin/env python

import sys


def find_routes(path, routes, cache) -> int:
    total = 0
    checkpoints = tuple(sorted(set(path) & {'dac', 'fft'}))

    for next_device in routes[path[-1]]:
        if (next_device, *checkpoints) in cache:
            total += cache[(next_device, *checkpoints)]
        elif next_device == 'out':
            if len(checkpoints) == 2:
                total += 1
        else:
            total += find_routes(path + (next_device, ), routes, cache)

    checkpoints = tuple(sorted(set(path[:-1]) & {'dac', 'fft'}))
    cache[(path[-1], *checkpoints)] = total
    return total



def main() -> None:
    routes = {}
    cache = {}

    for line in sys.stdin:
        device, outputs = line.split(':', maxsplit=1)
        routes[device] = set(outputs.split())

    print(find_routes(('svr', ), routes, cache))


if __name__ == '__main__':
    main()
