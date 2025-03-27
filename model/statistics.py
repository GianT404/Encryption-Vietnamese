# model/statistics.py

import json
import os
from datetime import datetime

# Một dictionary để lưu các thống kê
stats = {
    "algorithm_usage": {},   # ví dụ: {"Caesar": 10, "Vigenère": 5, ...}
    "total_files_processed": 0,
    "encryption_times": {},  # lưu danh sách thời gian thực hiện mã hóa cho từng thuật toán
}

def update_algorithm_usage(algorithm):
    stats["algorithm_usage"][algorithm] = stats["algorithm_usage"].get(algorithm, 0) + 1

def add_encryption_time(algorithm, elapsed_time):
    # elapsed_time tính bằng giây (float)
    if algorithm not in stats["encryption_times"]:
        stats["encryption_times"][algorithm] = []
    stats["encryption_times"][algorithm].append(elapsed_time)

def update_files_processed(count=1):
    stats["total_files_processed"] += count

def save_stats(file_path="stats.json"):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4)

def load_stats(file_path="stats.json"):
    global stats
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            stats = json.load(f)
    return stats

# model/statistics.py

def calculate_frequency(text):
    """
    Tính tần suất xuất hiện của từng ký tự trong text.
    Trả về dictionary: {character: frequency, ...}
    """
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def calculate_ic(text):
    """
    Tính chỉ số trùng lặp (Index of Coincidence) của văn bản.
    Công thức: IC = sum(n_i*(n_i-1)) / (N*(N-1)), với n_i là số lần xuất hiện ký tự i, N là tổng số ký tự.
    """
    freq = calculate_frequency(text)
    N = sum(freq.values())
    if N <= 1:
        return 0
    ic = sum(n*(n-1) for n in freq.values()) / (N*(N-1))
    return ic

def detect_language(text):
    """
    Một hàm đơn giản để "phát hiện" ngôn ngữ dựa trên chỉ số trùng lặp.
    Ví dụ: Nếu IC > 0.065, giả sử là English, ngược lại là Vietnamese.
    (Chỉ là ví dụ, bạn có thể điều chỉnh theo yêu cầu.)
    """
    ic = calculate_ic(text)
    if ic > 0.065:
        return "English"
    else:
        return "Vietnamese"

