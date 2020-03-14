from ui.projetor.window import *
from PyQt5.QtWidgets import QMainWindow

class ProjetorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.text = ''

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self.textLabel.setText(text)