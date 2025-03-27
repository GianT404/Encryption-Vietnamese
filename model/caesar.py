# model/caesar.py
from .constants import vietnamese_lower, vietnamese_upper

def encrypt(text, shift):
    result = ""
    for char in text:
        if char in vietnamese_lower:
            pos = vietnamese_lower.index(char)
            new_pos = (pos + shift) % len(vietnamese_lower)
            result += vietnamese_lower[new_pos]
        elif char in vietnamese_upper:
            pos = vietnamese_upper.index(char)
            new_pos = (pos + shift) % len(vietnamese_upper)
            result += vietnamese_upper[new_pos]
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

