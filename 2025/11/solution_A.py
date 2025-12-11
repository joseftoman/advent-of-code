#!/usr/bin/env python

import sys


def find_routes(device, routes) -> int:
    total = 0

    for next_device in routes[device]:
        if next_device == 'out':
            total += 1
        else:
            total += find_routes(next_device, routes)

    return total


def main() -> None:
    routes = {}

    for line in sys.stdin:
        device, outputs = line.split(':', maxsplit=1)
        routes[device] = set(outputs.split())

    print(find_routes('you', routes))


if __name__ == '__main__':
    main()
