import hashlib
import base64
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import time
from model.statistics import update_algorithm_usage, add_encryption_time, save_stats
def pad(data):
    pad_len = AES.block_size - (len(data) % AES.block_size)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt(plaintext, key):
    # Tạo khóa 256-bit từ key bằng SHA256
    key_hash = hashlib.sha256(key.encode('utf-8')).digest()
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode('utf-8'))
    encrypted_bytes = cipher.encrypt(padded_text)
    return base64.b64encode(iv + encrypted_bytes).decode('utf-8')

def aes_decrypt(ciphertext, key):
    key_hash = hashlib.sha256(key.encode('utf-8')).digest()
    encrypted_data = base64.b64decode(ciphertext)
    iv = encrypted_data[:AES.block_size]
    encrypted_bytes = encrypted_data[AES.block_size:]
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    padded_text = cipher.decrypt(encrypted_bytes)
    return unpad(padded_text).decode('utf-8')


