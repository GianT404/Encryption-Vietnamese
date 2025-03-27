# model/vigenere.py
from .constants import vietnamese_lower, vietnamese_upper

def encrypt(text, key):
    result = []
    key = key.strip()
    if not key:
        return text
    # Lọc key chỉ chứa các ký tự hợp lệ (đổi về chữ thường)
    key_clean = "".join([ch.lower() for ch in key if ch.lower() in vietnamese_lower])
    if not key_clean:
        return text
    key_len = len(key_clean)
    for i, char in enumerate(text):
        if char in vietnamese_lower:
            pos = vietnamese_lower.index(char)
            shift = vietnamese_lower.index(key_clean[i % key_len])
            new_pos = (pos + shift) % len(vietnamese_lower)
            result.append(vietnamese_lower[new_pos])
        elif char in vietnamese_upper:
            pos = vietnamese_upper.index(char)
            shift = vietnamese_lower.index(key_clean[i % key_len])
            new_pos = (pos + shift) % len(vietnamese_upper)
            result.append(vietnamese_upper[new_pos])
        else:
            result.append(char)
    return "".join(result)

def decrypt(text, key):
    result = []
    key = key.strip()
    if not key:
        return text
    key_clean = "".join([ch.lower() for ch in key if ch.lower() in vietnamese_lower])
    if not key_clean:
        return text
    key_len = len(key_clean)
    for i, char in enumerate(text):
        if char in vietnamese_lower:
            pos = vietnamese_lower.index(char)
            shift = vietnamese_lower.index(key_clean[i % key_len])
            new_pos = (pos - shift) % len(vietnamese_lower)
            result.append(vietnamese_lower[new_pos])
        elif char in vietnamese_upper:
            pos = vietnamese_upper.index(char)
            shift = vietnamese_lower.index(key_clean[i % key_len])
            new_pos = (pos - shift) % len(vietnamese_upper)
            result.append(vietnamese_upper[new_pos])
        else:
            result.append(char)
    return "".join(result)


