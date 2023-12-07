#!/usr/bin/python3

min_len = 35651584
data = '00111101111101000'
checksum = None

while len(data) < min_len:
    new = ''
    for ch in reversed(data):
        new += '1' if ch == '0' else '0'
    data = data + '0' + new

data = data[0:min_len]

while checksum is None or len(checksum) % 2 == 0:
    checksum = ''
    for i in range(0, len(data), 2):
        checksum += '1' if data[i] == data[i+1] else '0'
    data = checksum

print(checksum)
