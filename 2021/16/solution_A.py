#!/usr/bin/env python

import sys

packet = []
for char in list(sys.stdin.readline().rstrip()):
    packet.extend(list(bin(int(char, 16))[2:].zfill(4)))

versions = 0

def read_packet(packet, index):
    global versions

    version = int(''.join(packet[index:index+3]), 2)
    type_id = int(''.join(packet[index+3:index+6]), 2)
    length = 6
    index += 6
    versions += version

    if type_id == 4:
        while packet[index] == '1':
            length += 5
            index += 5

        length += 5
        index += 5
    else:
        len_type = packet[index]
        len_bits = 15 if len_type == '0' else 11
        index += 1
        sublen = int(''.join(packet[index:index+len_bits]), 2)
        index += len_bits
        length += 1 + len_bits
        
        if len_type == '0':
            while sublen:
                subpacket_len = read_packet(packet, index)
                length += subpacket_len
                index += subpacket_len
                sublen -= subpacket_len
        else:
            for _ in range(sublen):
                subpacket_len = read_packet(packet, index)
                length += subpacket_len
                index += subpacket_len

    return length


read_packet(packet, 0)
print(versions)
