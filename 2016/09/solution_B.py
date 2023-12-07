#!/usr/bin/python3

import sys
import re

def get_decomp_len(seq):
    max_pos = len(seq) - 1;
    pos = 0
    length = 0

    while pos <= max_pos:
        m_obj = regex.match(seq, pos);
        if m_obj:
            start = pos + len(m_obj.group(0))
            end = start + int(m_obj.group(1))
            length += int(m_obj.group(2)) * get_decomp_len(seq[start:end])
            pos += len(m_obj.group(0)) + int(m_obj.group(1))
        else:
            pos += 1
            length += 1

    return length

regex = re.compile('\((\d+)x(\d+)\)');
input = sys.stdin.readline().rstrip()
print(get_decomp_len(input))
