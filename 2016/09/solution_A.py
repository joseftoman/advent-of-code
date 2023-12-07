#!/usr/bin/python3

import sys
import re

input = sys.stdin.readline().rstrip()
max_pos = len(input) - 1;
pos = 0
length = 0
regex = re.compile('\((\d+)x(\d+)\)');

while pos <= max_pos:
    m_obj = regex.match(input, pos);
    if m_obj:
        pos += len(m_obj.group(0)) + int(m_obj.group(1))
        length += int(m_obj.group(1)) * int(m_obj.group(2))
    else:
        pos += 1
        length += 1

print(length)
