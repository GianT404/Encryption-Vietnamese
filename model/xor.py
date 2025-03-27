# model/xor.py

def xor_encrypt(text, key):
    if not key:
        return text  # Nếu khóa rỗng, trả về text gốc
    
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        # Lấy ký tự từ khóa theo chu kỳ và thực hiện XOR trên mã ASCII (hoặc Unicode)
        xor_char = chr(ord(char) ^ ord(key[i % key_length]))
        result.append(xor_char)
    return "".join(result)

xor_decrypt = xor_encrypt
