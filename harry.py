import os

from conda.gateways.repodata.jlap.core import keyed_hash
from cryptography.fernet import Fernet

virustotal = 'https://www.virustotal.com/gui/home/upload'
# Getting all the files for decryption
files = []
for file in os.listdir():
    if file.endswith(".py") or file.endswith(".key"):
        continue
    if os.path.isfile(file):
        files.append(file)

# Loading the key
with open("decryption-key.key", 'rb') as thekey:
    key = thekey.read()

# Decrypting the files
def decrypt_data():
    for file in files:
        with open(file, 'rb') as thefile:
            data = thefile.read()
        decrypted_data = Fernet(key).decrypt(data)
        with open(file, 'wb') as thefile:
            thefile.write(decrypted_data)
    print(f"Your files are decrypted. Scan everything on Virustotal -> {virustotal} before executing it.")

decrypt_data()