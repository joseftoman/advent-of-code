#!/usr/bin/python3

import sys
import re

ok = 0

for line in sys.stdin:
    required = re.search(r'(.)(?!\1)(.)\2\1', line)
    forbidden = re.search(r'\[[^[\]]*(.)(?!\1)(.)\2\1[^[\]]*\]', line)
    if forbidden is None and required is not None and required.group(1) != required.group(2): ok += 1

print(ok)
