# controller.py
import time
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets
import os
from model.transposition import rail_fence_encrypt, rail_fence_decrypt
from model.xor import xor_encrypt, xor_decrypt
from model import (
    caesar_encrypt, caesar_decrypt,
    vigenere_encrypt, vigenere_decrypt,
    belasco_encrypt, belasco_decrypt
)
from model.logger import logger
from model.aes import aes_encrypt, aes_decrypt
from model.rsa import rsa_encrypt, rsa_decrypt
from model.statistics import update_algorithm_usage, add_encryption_time, update_files_processed, save_stats

class CipherController:
    def __init__(self, view):
        self.view = view
        self.setup_treeview()
        self.connect_signals()
    
    def setup_treeview(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Các kỹ thuật mã hóa"])
        # Nhóm 1: Kỹ thuật thay thế
        group1 = QStandardItem("Kỹ thuật thay thế")

        group1.appendRow(QStandardItem("Caesar"))
        group1.appendRow(QStandardItem("Vigenère"))
        group1.appendRow(QStandardItem("Belasco"))
        
        # Nhóm 2: Kỹ thuật chuyển vị
        group2 = QStandardItem("Kỹ thuật chuyển vị")
        group2.appendRow(QStandardItem("Chuyển vị 2 dòng"))
        group2.appendRow(QStandardItem("Chuyển vị nhiều dòng"))

        group3 = QStandardItem("Kỹ thuật XOR")
        group3.appendRow(QStandardItem("XOR"))

        # Nhóm Kỹ thuật thay thế hiện đại
        group_modern = QStandardItem("Kỹ thuật hiện đại")
        group_modern.appendRow(QStandardItem("AES"))
        group_modern.appendRow(QStandardItem("RSA"))
        
        group4 = QStandardItem("Nhóm 9")
        group4.appendRow(QStandardItem("Thông tin thành viên"))
        
        model.appendRow(group1)
        model.appendRow(group2)
        model.appendRow(group3)
        model.appendRow(group_modern)
        model.appendRow(group4)
        
        self.view.treeView.setModel(model)
        self.view.treeView.expandAll()  # Mở rộng toàn bộ cây
        pass


    def connect_signals(self):
        self.view.treeView.clicked.connect(self.on_treeview_clicked)
        # Kết nối các button mã hóa/giải mã (đảm bảo objectName của button khớp với file UI)
        self.view.encryptButton.clicked.connect(self.encrypt_text)
        self.view.decryptButton.clicked.connect(self.decrypt_text)
        self.view.encryptButton_2.clicked.connect(self.encrypt_text)
        self.view.decryptButton_2.clicked.connect(self.decrypt_text)
        self.view.encryptButton_3.clicked.connect(self.encrypt_text)
        self.view.decryptButton_3.clicked.connect(self.decrypt_text)
        self.view.encryptButton_4.clicked.connect(self.encrypt_text)
        self.view.decryptButton_4.clicked.connect(self.decrypt_text)
        self.view.encryptButton_5.clicked.connect(self.encrypt_text)
        self.view.decryptButton_5.clicked.connect(self.decrypt_text)
        self.view.encryptButton_6.clicked.connect(self.encrypt_text)
        self.view.decryptButton_6.clicked.connect(self.decrypt_text)
        self.view.encryptButton_7.clicked.connect(self.encrypt_text)
        self.view.decryptButton_7.clicked.connect(self.decrypt_text)
        self.view.encryptButton_8.clicked.connect(self.encrypt_text)
        self.view.decryptButton_8.clicked.connect(self.decrypt_text)
        self.view.logoutButton.clicked.connect(self.handle_logout)
        self.view.openFileButton.clicked.connect(self.open_file)
        self.view.saveFileButton.clicked.connect(self.save_file)
        self.view.reportButton.clicked.connect(self.open_report_viewer)
    def open_report_viewer(self):
        from view.report_view import ReportViewer
        self.report_viewer = ReportViewer("stats.json")
        self.report_viewer.show()

    def on_treeview_clicked(self, index):
        cipher = index.data()
        print("Đã chọn thuật toán:", cipher)
        if cipher == "Caesar":
            self.view.stackWidget.setCurrentIndex(0)
        elif cipher == "Vigenère":
            self.view.stackWidget.setCurrentIndex(1)
        elif cipher == "Belasco":
            self.view.stackWidget.setCurrentIndex(2)
        elif cipher == "Chuyển vị 2 dòng":
            self.view.stackWidget.setCurrentIndex(3)
        elif cipher == "Chuyển vị nhiều dòng":
            self.view.stackWidget.setCurrentIndex(4)
        elif cipher in ("XOR", "Kỹ thuật XOR"):
            self.view.stackWidget.setCurrentIndex(5)
        elif cipher == "AES":
            self.view.stackWidget.setCurrentIndex(6)
        elif cipher == "RSA":
            self.view.stackWidget.setCurrentIndex(7)
        elif cipher in ("Nhóm 9", "Thông tin thành viên"):
            self.view.stackWidget.setCurrentIndex(8)

    
    def encrypt_text(self):
        start_time = time.time()
        cipher = self.view.treeView.currentIndex().data()
        current_page = self.view.stackWidget.currentWidget()
        print("Đang ở trang:", current_page)
        
        # Khai báo ban đầu
        input_widget = None
        key_widget = None
        output_widget = None
        result = ""
        
        if cipher == "Caesar":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "inputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "keyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "outputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            try:
                shift = int(key)
            except ValueError:
                shift = 3  # Giá trị mặc định nếu key không hợp lệ
            result = caesar_encrypt(text, shift)
            update_algorithm_usage("Caesar")
            
        elif cipher == "Vigenère":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "vigenereInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "vigenereKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "vigenereOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            result = vigenere_encrypt(text, key)
            update_algorithm_usage("Vigenère")
            
        elif cipher == "Belasco":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "belascoInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "belascoKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "belascoOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            result = belasco_encrypt(text, key)
            update_algorithm_usage("Belasco")
            
        elif cipher == "Chuyển vị 2 dòng":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionInputText")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            result = rail_fence_encrypt(text, 2)
            update_algorithm_usage("Chuyển vị 2 dòng")
            
        elif cipher == "Chuyển vị nhiều dòng":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionInputText_2")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "transpositionKeyLineEdit_2")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionOutputText_2")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            try:
                rails = int(key)
            except ValueError:
                rails = 3
            result = rail_fence_encrypt(text, rails)
            update_algorithm_usage("Chuyển vị nhiều dòng")
            
        elif cipher == "XOR":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "xorInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "xorKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "xorOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            result = xor_encrypt(text, key)
            update_algorithm_usage("XOR")
            
        elif cipher == "AES":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "aesInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "aesKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "aesOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            try:
                result = aes_encrypt(text, key)
            except Exception as e:
                result = f"Lỗi AES: {str(e)}"
            update_algorithm_usage("AES")
            
        elif cipher == "RSA":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "rsaInputText")
                    key_widget = current_page.findChild(QtWidgets.QLineEdit, "rsaKeyLineEdit")
                    output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "rsaOutputText")
                    text = input_widget.toPlainText() if input_widget else ""
                    key = key_widget.text() if key_widget else ""
                    update_algorithm_usage("RSA")
                    try:
                        rails = int(key)
                    except ValueError:
                        rails = 3
                    result = rail_fence_encrypt(text, rails)
        else:
                    result = "Chưa chọn thuật toán!"
        
        # Tính thời gian mã hóa và lưu thống kê thời gian
        elapsed_time = time.time() - start_time
        add_encryption_time(cipher, elapsed_time)
        save_stats()
        
        print("Text nhập:", text)
        if key_widget:
            print("Key nhập:", key)
        print("Kết quả mã hóa:", result)
        
        if output_widget:
            output_widget.setPlainText(result)
        else:
            QtWidgets.QMessageBox.warning(self.view, "Cảnh báo", "Không tìm thấy ô hiển thị kết quả!")

    
    def decrypt_text(self):
        cipher = self.view.treeView.currentIndex().data()
        current_page = self.view.stackWidget.currentWidget()
        result = ""
        
        if cipher == "Caesar":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "inputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "keyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "outputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            try:
                shift = int(key)
            except ValueError:
                shift = 3
            result = caesar_decrypt(text, shift)
        elif cipher == "Vigenère":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "vigenereInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "vigenereKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "vigenereOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            result = vigenere_decrypt(text, key)
        elif cipher == "Belasco":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "belascoInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "belascoKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "belascoOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            result = belasco_decrypt(text, key)
        elif cipher == "Chuyển vị 2 dòng":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionInputText")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            result = rail_fence_decrypt(text, 2)
        elif cipher == "Chuyển vị nhiều dòng":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionInputText_2")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "transpositionKeyLineEdit_2")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionOutputText_2")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
        elif cipher == "XOR":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "xorInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "xorKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "xorOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            result = xor_decrypt(text, key)  # Chỉ gọi hàm XOR, không gọi rail_fence_decrypt
        elif cipher == "AES":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "aesInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "aesKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "aesOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
        elif cipher ==  "RSA":
            input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "rsaInputText")
            key_widget = current_page.findChild(QtWidgets.QLineEdit, "rsaKeyLineEdit")
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "rsaOutputText")
            text = input_widget.toPlainText() if input_widget else ""
            key = key_widget.text() if key_widget else ""
            try:
                rails = int(key)
            except ValueError:
                rails = 3
            result = rail_fence_decrypt(text, rails)
        else:
            result = "Chưa chọn thuật toán!"
        
        if output_widget:
            output_widget.setPlainText(result)

    def handle_logout(self):
        # Đóng cửa sổ chính
        self.view.close()
        # Mở lại cửa sổ đăng nhập
        from login_controller import LoginController
        self.login_controller = LoginController()
        self.login_controller.login_window.show()
        logger.info("Đăng xuất khỏi hệ thống.")
    def open_file(self):
        # Mở hộp thoại mở file
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.view,
            "Mở file mã hóa",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    file_content = f.read()
                # Giả sử bạn muốn hiển thị nội dung file vào ô input của trang hiện tại
                current_page = self.view.stackWidget.currentWidget()
                # Lấy tên thuật toán đang chọn
                cipher = self.view.treeView.currentIndex().data()
                # Xác định widget input theo thuật toán
                if cipher == "Caesar":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "inputText")
                    update_files_processed(1)
                    save_stats()
                elif cipher == "Vigenère":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "vigenereInputText")
                    update_files_processed(2)
                    save_stats()
                elif cipher == "Belasco":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "belascoInputText")
                    update_files_processed(3)
                    save_stats()
                elif cipher == "XOR":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "xorInputText")
                    update_files_processed(4)
                    save_stats()
                elif cipher == "Chuyển vị 2 dòng":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionInputText")
                    update_files_processed(5)
                    save_stats()
                elif cipher == "Chuyển vị nhiều dòng":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionInputText_2")
                    update_files_processed(6)
                    save_stats()
                elif cipher == "AES":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "aesInputText")
                    update_files_processed(7)
                    save_stats()
                elif cipher == "RSA":
                    input_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "rsaInputText")
                    update_files_processed(8)
                    save_stats()
                else:
                    input_widget = None

                if input_widget:
                    # Tùy vào thiết kế, bạn có thể cho hiển thị file vào ô input
                    input_widget.setPlainText(file_content)
                    QtWidgets.QMessageBox.information(self.view, "Thành công", "Mở file thành công!")
                else:
                    QtWidgets.QMessageBox.warning(self.view, "Cảnh báo", "Không tìm thấy ô nhập liệu phù hợp!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", f"Không đọc được file: {str(e)}")

    def save_file(self):
        current_page = self.view.stackWidget.currentWidget()
        cipher = self.view.treeView.currentIndex().data()
        
        # Xác định ô hiển thị kết quả dựa theo thuật toán
        if cipher == "Caesar":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "outputText")
        elif cipher == "Vigenère":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "vigenereOutputText")
        elif cipher == "Belasco":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "belascoOutputText")
        elif cipher == "XOR":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "xorOutputText")
        elif cipher == "Chuyển vị 2 dòng":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionOutputText")
        elif cipher == "Chuyển vị nhiều dòng":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "transpositionOutputText_2")
        elif cipher == "AES":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "aesOutputText")
        elif cipher == "RSA":
            output_widget = current_page.findChild(QtWidgets.QPlainTextEdit, "rsaOutputText")
        else:
            output_widget = None

        if output_widget is None:
            QtWidgets.QMessageBox.warning(self.view, "Cảnh báo", "Không tìm thấy ô hiển thị kết quả!")
            return

        content = output_widget.toPlainText()
        if not content:
            QtWidgets.QMessageBox.information(self.view, "Thông báo", "Không có nội dung để lưu!")
            return

        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.view,
            "Lưu kết quả mã hóa",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(content)
                QtWidgets.QMessageBox.information(self.view, "Thành công", "Lưu file thành công!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self.view, "Lỗi", f"Lỗi khi lưu file: {str(e)}")