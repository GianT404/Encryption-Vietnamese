import os
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui_file="cipher.ui"):
        super().__init__()
        uic.loadUi(ui_file, self)