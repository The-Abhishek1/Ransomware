🔐 Ransomware Script in Python
A powerful yet simple Python-based ransomware script that encrypts all files in the current directory. Users can unlock their files 🔓 by entering the correct passphrase.

🌟 Features
✅ Key Generation: Generate a secure encryption key with the keygen.py script.
✅ File Encryption: Encrypt all files in the directory using ransomware.py.
✅ File Decryption: Unlock your files with the right passphrase using decr.py.
✅ Secure Modules:

📂 os: File operations.
🛡️ cryptography: Handles encryption and decryption securely.

📂 Folder Structure
📌 keygen.py: Generates an encryption key and saves it in key.key.
📌 ransomware.py: Encrypts all files in the current directory.
📌 decr.py: Decrypts encrypted files using the generated key and passphrase.
📌 key.key: Stores the auto-generated encryption key.

⚙️ Setup & Installation

🐍 Install Python 3.x.
🛠️ Install required dependencies:
    pip install cryptography  

🚀 How to Use
Step 1: 🔑 Generate the Key
Run keygen.py to generate a secure encryption key:
python keygen.py  

Step 2: 🔒 Encrypt Files
Run ransomware.py to encrypt all files in the directory:
python ransomware.py 
 
Your files will be encrypted and inaccessible until decrypted.

Step 3: 🔓 Decrypt Files
Run decr.py to decrypt the files:
python decr.py  

Enter the correct passphrase to unlock your files.

⚠️ Disclaimer
This script is created for educational purposes only. Misuse of ransomware can have severe legal and ethical consequences. Use responsibly. 🙏