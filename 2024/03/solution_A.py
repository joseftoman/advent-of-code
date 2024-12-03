#!/usr/bin/env python

import re
import sys

print(sum(int(_[0]) * int(_[1]) for _ in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', ''.join(sys.stdin))))
