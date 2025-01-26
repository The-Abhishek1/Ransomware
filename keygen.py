from cryptography.fernet import Fernet


key = Fernet.generate_key()
with open('key.key', 'wb') as thekey:
    thekey.write(key)

print(key)
