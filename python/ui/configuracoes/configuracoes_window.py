from ui.configuracoes.window import *
from PyQt5.QtWidgets import QMainWindow

class ConfiguracoesWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)