# model/belasco.py
from .constants import vietnamese_lower, vietnamese_upper

def generate_mapping(key):
    # Xử lý key: loại bỏ ký tự trùng lặp và chỉ lấy ký tự có trong bảng chữ cái
    key_processed_lower = ""
    for ch in key.lower():
        if ch in vietnamese_lower and ch not in key_processed_lower:
            key_processed_lower += ch
    remaining_lower = "".join([c for c in vietnamese_lower if c not in key_processed_lower])
    cipher_alphabet_lower = key_processed_lower + remaining_lower

    key_processed_upper = ""
    for ch in key.upper():
        if ch in vietnamese_upper and ch not in key_processed_upper:
            key_processed_upper += ch
    remaining_upper = "".join([c for c in vietnamese_upper if c not in key_processed_upper])
    cipher_alphabet_upper = key_processed_upper + remaining_upper

    mapping_lower = {vietnamese_lower[i]: cipher_alphabet_lower[i] for i in range(len(vietnamese_lower))}
    mapping_upper = {vietnamese_upper[i]: cipher_alphabet_upper[i] for i in range(len(vietnamese_upper))}
    mapping = {}
    mapping.update(mapping_lower)
    mapping.update(mapping_upper)
    return mapping

def encrypt(text, key):
    mapping = generate_mapping(key)
    result = ""
    for ch in text:
        if ch in mapping:
            result += mapping[ch]
        else:
            result += ch
    return result

def decrypt(text, key):
    mapping = generate_mapping(key)
    inv_mapping = {v: k for k, v in mapping.items()}
    result = ""
    for ch in text:
        if ch in inv_mapping:
            result += inv_mapping[ch]
        else:
            result += ch
    return result
