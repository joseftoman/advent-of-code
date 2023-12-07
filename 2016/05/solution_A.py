#!/usr/bin/python3

import hashlib

prefix = "ojvtpuvg"
index = 0
code = ''

while len(code) < 8:
    digest = hashlib.md5((prefix+str(index)).encode("utf-8")).hexdigest()
    if digest[:5] == '00000': code += digest[5]
    index += 1

print(code)
