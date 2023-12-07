#!/usr/bin/env python

import sys

packet = []
for char in list(sys.stdin.readline().rstrip()):
    packet.extend(list(bin(int(char, 16))[2:].zfill(4)))

def read_packet(packet, index):
    type_id = int(''.join(packet[index+3:index+6]), 2)
    #print('INIT:', index, type_id)
    length = 6
    index += 6

    if type_id == 4:
        num = ''

        while packet[index] == '1':
            num += ''.join(packet[index+1:index+5])
            length += 5
            index += 5

        num += ''.join(packet[index+1:index+5])
        length += 5
        index += 5

        #print('LITERAL:', int(num, 2))
        return length, int(num, 2)

    len_type = packet[index]
    len_bits = 15 if len_type == '0' else 11
    index += 1
    sublen = int(''.join(packet[index:index+len_bits]), 2)
    index += len_bits
    length += 1 + len_bits
    #print('OP:', len_type, sublen)
    args = []
    
    if len_type == '0':
        while sublen:
            subpacket_len, arg = read_packet(packet, index)
            length += subpacket_len
            index += subpacket_len
            sublen -= subpacket_len
            args.append(arg)
    else:
        for _ in range(sublen):
            subpacket_len, arg = read_packet(packet, index)
            length += subpacket_len
            index += subpacket_len
            args.append(arg)

    #print('ARGS:', args)
    value = None

    if type_id == 0:
        value = 0
        for arg in args:
            value += arg
    elif type_id == 1:
        value = 1
        for arg in args:
            value *= arg
    elif type_id == 2:
        value = min(args)
    elif type_id == 3:
        value = max(args)
    elif type_id == 5:
        value = 1 if args[0] > args[1] else 0
    elif type_id == 6:
        value = 1 if args[0] < args[1] else 0
    elif type_id == 7:
        value = 1 if args[0] == args[1] else 0

    #print('VALUE:', value)
    return length, value


_, value = read_packet(packet, 0)
print(value)
