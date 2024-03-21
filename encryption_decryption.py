from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64

def pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def encrypt(message, password):
    key = PBKDF2(password, b'salt', 16, 1000)
    message = pad(message)
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(iv + encrypted)

def decrypt(ciphertext, password):
    key = PBKDF2(password, b'salt', 16, 1000)
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext[AES.block_size:])
    return unpad(decrypted).decode('utf-8')
