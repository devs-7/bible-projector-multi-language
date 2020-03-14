from ui.main_view.view import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)