from ui.projetor.window import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QKeyEvent
from PyQt5 import QtCore


class ProjetorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.text = ''

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self.textLabel.setText(text)
