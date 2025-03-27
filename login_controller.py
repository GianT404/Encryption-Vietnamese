from PyQt5 import QtWidgets
from model.auth import register, login
from view.login_view import LoginWindow
from controller import CipherController
from view.view import CipherView
from model.logger import logger

class LoginController:
    def __init__(self):
        self.login_window = LoginWindow()
        self.login_window.loginButton.clicked.connect(self.handle_login)
        self.login_window.registerButton.clicked.connect(self.handle_register)
    
    def handle_login(self):
        username = self.login_window.usernameLineEdit.text()
        password = self.login_window.passwordLineEdit.text()
        logger.info(f"Người dùng cố gắng đăng nhập với username: {username}")
        success, msg = login(username, password)
        self.login_window.messageLabel.setText(msg)
        if success:
            logger.info(f"Đăng nhập thành công: {username}")
            self.open_cipher_window()
        else:
            logger.warning(f"Đăng nhập thất bại cho username: {username}")
    
    def handle_register(self):
        username = self.login_window.usernameLineEdit.text()
        password = self.login_window.passwordLineEdit.text()
        logger.info(f"Người dùng đăng ký với username: {username}")
        success, msg = register(username, password)
        self.login_window.messageLabel.setText(msg)
        if success:
            logger.info(f"Đăng ký thành công: {username}")
        else:
            logger.warning(f"Đăng ký thất bại cho username: {username} - {msg}")
    
    def open_cipher_window(self):
        self.cipher_view = CipherView("cipher.ui")
        self.cipher_controller = CipherController(self.cipher_view)
        self.cipher_view.show()
        logger.info("Chuyển sang màn hình Cipher sau khi đăng nhập thành công")
        self.login_window.close()