# Mã hóa ngôn ngữ tiếng việt

Chương trình mã hóa đa thuật toán được xây dựng bằng Python và PyQt5. Ứng dụng hỗ trợ nhiều thuật toán mã hóa và giải mã, từ các phương pháp cổ điển như Caesar, Vigenère, Belasco, Chuyển vị (Rail Fence), XOR cho đến các thuật toán hiện đại như AES và RSA. Ngoài ra, ứng dụng còn tích hợp các tính năng phụ như đăng nhập/đăng ký, lưu trữ log hoạt động, xem báo cáo thống kê, xuất và mở file mã hóa.

## Tính Năng Chính

- **Mã hóa & Giải mã:**
  - **Caesar Cipher:** Mã hóa dựa trên độ dịch chuyển (shift) của các ký tự.
  - **Vigenère Cipher:** Mã hóa dựa trên một chuỗi khóa.
  - **Belasco Cipher:** Mã hóa bằng kỹ thuật thay thế ký tự dựa trên chuỗi khóa.
  - **Chuyển vị (Rail Fence):** Sắp xếp lại thứ tự các ký tự theo dạng "cây chữ" với số dòng (rail) xác định.
  - **XOR Encryption:** Mã hóa bằng phép XOR với một chuỗi khóa.
  - **AES Encryption:** Sử dụng thuật toán AES (CBC) với khóa được tạo từ chuỗi key thông qua SHA-256.
  - **RSA Encryption:** Sử dụng cặp khóa RSA (Public Key/Private Key) để mã hóa và giải mã.

- **Quản lý Tài Khoản:**
  - Đăng ký và đăng nhập.
  - Mã hóa thông tin tài khoản.

- **Tính Năng Upload & Lưu File:**
  - Upload file văn bản để mã hóa nội dung.
  - Lưu kết quả mã hóa/giải mã ra file.

- **Log Hoạt Động & Báo Cáo:**
  - Ghi log các hoạt động của người dùng (đăng nhập, mã hóa, giải mã, upload file, ...).
  - Màn hình báo cáo thống kê với biểu đồ trực quan hiển thị số lần sử dụng thuật toán, thời gian thực hiện, số file xử lý, v.v.

## Cài Đặt & Chạy Ứng Dụng

1. **Cài đặt Python và các thư viện cần thiết:**

   - Python 3.x  
   - PyQt5: `pip install PyQt5`  
   - PyCryptodomeX (cho AES, RSA):  
     ```bash
     pip install pycryptodomex
     ```
   - Các thư viện khác (nếu có).

