import os
from PyQt5 import uic, QtWidgets

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "login.ui")
        uic.loadUi(ui_path, self)
