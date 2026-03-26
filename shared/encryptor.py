import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad    

class Encryptor():
    def __init__(self, key):
        self.key = bytes.fromhex(key)
        

    def encrypt(self, data):
        iv = os.urandom(16)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = self.cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(iv + encrypted).decode()

    def decrypt(self, data):
        data = base64.b64decode(data)
        iv = data[:16]
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(self.cipher.decrypt(data[16:]), AES.block_size).decode()

