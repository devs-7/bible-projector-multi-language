from PyQt5.QtWidgets import QMainWindow
from src.ui.configuracoes.window import *


class ConfiguracoesWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
