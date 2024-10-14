# Ransomware

> **Disclaimer**: This repository is intended for **educational purposes only**. The scripts provided here demonstrate how encryption and decryption work, mimicking the functionality of ransomware. Understanding these concepts is vital for learning cybersecurity. Python is a powerful language that enables you to write a wide range of scripts, including security tools. Misuse of this knowledge for malicious intent is strictly prohibited.

This repository contains Python scripts that allow you to **encrypt** and **decrypt** files in a directory. The encryption uses the `cryptography.fernet` module to securely encrypt files, while the decryption script restores the original files using the generated key.

> **Note**: Windows Defender and other antivirus software may detect and delete these scripts if they are not obfuscated. Ensure you obfuscate the code before executing it to avoid deletion.

## Features
- **Encrypts** all files in the current directory (excluding `.py` and `.key` files).
- **Decrypts** files using the saved encryption key.
- Automatically generates and saves a decryption key.
- Easy-to-use Python scripts that can be run from the command line.

## Files
- `scary.py`: This script encrypts all files in the current directory.
- `harry.py`: This script decrypts the files encrypted by `scary.py`.
- `decryption-key.key`: The encryption/decryption key file generated during encryption.

## Requirements

Ensure you have Python installed, along with the `cryptography` package. You can install the required dependencies using:

```bash
pip install cryptography
```

## Usage

### Encryption
1. Place the `scary.py` file in the directory where you want to encrypt the files.
2. Run the script:

```bash
python scary.py
```
This will encrypt all files in the directory (except `.py` and `.key` files) and generate a `decryption-key.key` file.

### Decryption
1. Ensure the `decryption-key.key` is present in the directory where you want to decrypt the files.
2. Run the script:

```bash
python harry.py
```
This will decrypt all previously encrypted files in the directory.

### Important: Obfuscate Before Execution
To prevent Windows Defender or other antivirus software from flagging and deleting the scripts, it is crucial to **obfuscate the code** before running them. This step ensures the scripts run smoothly without interference from security software.

You can use tools like `pyarmor` or `pyminifier` for obfuscation. Here’s a simple way to obfuscate the scripts using `pyminifier`:

1. Install `pyminifier`:
   ```bash
   pip install pyminifier
   ```

2. Obfuscate your script:
   ```bash
   pyminifier --obfuscate encrypt.py > encrypt_obfuscated.py
   pyminifier --obfuscate decrypt.py > decrypt_obfuscated.py
   ```

## Security Warning

This script is for **educational purposes** only. It should not be used for any malicious activity or unauthorized encryption/decryption of files.

---

Feel free to adjust any sections to better fit your style or additional details you want to include!
