import os
from cryptography.fernet import Fernet

# Dictionary lưu trữ tài khoản trong bộ nhớ: username -> password (plaintext)
users = {}

# Xác định thư mục và file để lưu dữ liệu
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data")
ACCOUNTS_FILE = os.path.join(DATA_FOLDER, "accounts.txt")
KEY_FILE = os.path.join(DATA_FOLDER, "key.key")


def get_key():
    """Lấy key mã hóa từ file KEY_FILE, nếu không có thì tạo mới và lưu lại."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

# Tạo đối tượng Fernet từ key
fernet = Fernet(get_key())

def load_accounts():
    """Nạp các tài khoản từ file ACCOUNTS_FILE đã được mã hóa, 
       mỗi dòng có định dạng: mã hóa của 'username:password'
    """
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "rb") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                try:
                    decrypted = fernet.decrypt(line).decode("utf-8")
                    parts = decrypted.split(":", 1)
                    if len(parts) == 2:
                        username, password = parts
                        users[username] = password
                except Exception as e:
                    print("Lỗi giải mã dòng:", e)

# Nạp tài khoản khi module được import
load_accounts()

def register(username, password):
    """Đăng ký tài khoản mới:
       - Kiểm tra điều kiện (username không rỗng, password ít nhất 6 ký tự, tài khoản chưa tồn tại)
       - Mã hóa thông tin tài khoản và lưu vào file
    """
    if not username:
        return False, "Username không được để trống!"
    if len(password) < 6:
        return False, "Password phải có ít nhất 6 ký tự!"
    if username in users:
        return False, "Tài khoản đã tồn tại!"
    
    # Lưu vào bộ nhớ (plaintext)
    users[username] = password
    # Tạo chuỗi "username:password" và mã hóa
    account_line = f"{username}:{password}"
    try:
        encrypted_line = fernet.encrypt(account_line.encode("utf-8"))
        with open(ACCOUNTS_FILE, "ab") as f:
            f.write(encrypted_line + b"\n")
    except Exception as e:
        return False, f"Lỗi khi lưu tài khoản: {str(e)}"
    
    return True, "Đăng ký thành công!"

def login(username, password):
    """Đăng nhập bằng cách so sánh thông tin nhập với dữ liệu đã tải (plaintext) trong bộ nhớ."""
    if username in users and users[username] == password:
        return True, "Đăng nhập thành công!"
    return False, "Sai thông tin đăng nhập!"
