import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def generate_keys(key_size=2048):
    """
    Tạo cặp khóa RSA (public và private) với kích thước key_size (2048 bits mặc định).
    Trả về tuple (public_key, private_key) dưới dạng bytes.
    """
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def rsa_encrypt(plaintext, public_key):
    """
    Mã hóa chuỗi plaintext sử dụng RSA với public_key.
    - plaintext: chuỗi cần mã hóa.
    - public_key: public key dưới dạng bytes hoặc chuỗi (nếu chuỗi, convert về bytes).
    Trả về ciphertext dưới dạng chuỗi base64.
    """
    if isinstance(public_key, str):
        public_key = public_key.encode('utf-8')
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_bytes = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def rsa_decrypt(ciphertext, private_key):
    """
    Giải mã ciphertext (dạng chuỗi base64) sử dụng RSA với private_key.
    - ciphertext: chuỗi base64 chứa dữ liệu đã mã hóa.
    - private_key: private key dưới dạng bytes hoặc chuỗi.
    Trả về plaintext gốc.
    """
    if isinstance(private_key, str):
        private_key = private_key.encode('utf-8')
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_bytes = base64.b64decode(ciphertext)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return decrypted_bytes.decode('utf-8')
