#!/usr/bin/python3

import sys

components = []
c_map = {}
max_bridge = [ 0, 0 ]

for line in [ l.rstrip() for l in sys.stdin ]:
    ports = tuple([ int(x) for x in line.split('/') ])
    unique = tuple(ports) if ports[0] != ports[1] else tuple([ports[0]])
    components.append([ports, unique, False])

    for port in unique:
        if port not in c_map: c_map[port] = {}
        c_map[port][len(components) - 1] = True

def add_component(port, strength, length):
    global max_bridge

    if len(c_map[port]) == 0:
        if length > max_bridge[0] or (length == max_bridge[0] and strength > max_bridge[1]): max_bridge = [ length, strength ]
        return

    available = c_map[port].keys()
    for pos in available:
        c = components[pos]
        c[2] = length
        for p in c[1]: del c_map[p][pos]
        other = c[0][0] if c[0][0] != port else c[0][1]

        add_component(other, strength + c[0][0] + c[0][1], length + 1)

        for p in c[1]: c_map[p][pos] = True
        c[2] = False

add_component(0, 0, 0)
print(max_bridge[1])
