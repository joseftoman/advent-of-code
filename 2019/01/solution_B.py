#!/usr/bin/env python

import sys
fuel = 0

for line in sys.stdin:
    module_fuel = int(line)
    while module_fuel > 0:
        module_fuel = int(module_fuel / 3) - 2
        if module_fuel > 0:
            fuel += module_fuel

print(fuel)
