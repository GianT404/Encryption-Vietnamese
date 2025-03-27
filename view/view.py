import os
from PyQt5 import QtWidgets, uic
import os

class CipherView(QtWidgets.QMainWindow):
    def __init__(self, ui_file="cipher.ui"):
        super().__init__()
        # Tính đường dẫn đến file .ui nằm cùng thư mục với file view.py
        ui_path = os.path.join(os.path.dirname(__file__), ui_file)
        print("Loading UI from:", ui_path)  # Debug: in ra đường dẫn
        uic.loadUi(ui_path, self)
        self.toolbar = self.addToolBar("Main Toolbar")