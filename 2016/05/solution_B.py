#!/usr/bin/python3

import hashlib

prefix = "ojvtpuvg"
index = 0
code = '--------'
done = 0

while done < 8:
    digest = hashlib.md5((prefix+str(index)).encode("utf-8")).hexdigest()
    index += 1
    if digest[:5] == '00000' and 48 <= ord(digest[5]) <= 55 and code[int(digest[5])] == '-':
        code = code[:int(digest[5])] + digest[6] + code[int(digest[5])+1:]
        done += 1

print(code)
