import sys
from PyQt5 import QtWidgets
import logging
from login_controller import LoginController

def on_exit():
    logging.info("Người dùng đã thoát chương trình.")

def main():
    app = QtWidgets.QApplication(sys.argv)
     # Ghi log ngay khi ứng dụng bắt đầu
    logging.info("Ứng dụng bắt đầu chạy.")
    # Kết nối tín hiệu aboutToQuit để ghi log khi ứng dụng tắt
    app.aboutToQuit.connect(on_exit)
    
    global login_controller
    login_controller = LoginController()
    login_controller.login_window.show()
    
    exit_code = app.exec_()
    # Đảm bảo flush log trước khi thoát
    logging.shutdown()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
