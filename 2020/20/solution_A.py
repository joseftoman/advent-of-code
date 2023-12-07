#!/usr/bin/env python

import re
import sys

from grid import get_grid

grid, edges = get_grid()
print(grid[(edges['left'], edges['top'])].id * grid[(edges['left'], edges['bottom'])].id * grid[(edges['right'], edges['top'])].id * grid[(edges['right'], edges['bottom'])].id)
