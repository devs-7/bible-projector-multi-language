from model.bible import Bible, format_reference
from ui.projetor.projetor_window import ProjetorWindow

from ui.main.window import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QKeyEvent
from PyQt5 import QtCore

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.bible = Bible()
        self.projetor_window = ProjetorWindow()

        self.pesquisarButton.clicked.connect(self.pesquisar)
        self.projetarButton.clicked.connect(self.projetar)
        self.pesquisaLineEdit.returnPressed.connect(self.pesquisar)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == QtCore.Qt.Key_F4:
            self.pesquisaLineEdit.setFocus(True)
            self.pesquisaLineEdit.selectAll()
        elif key == QtCore.Qt.Key_F5:
            self.projetar()
        elif key == QtCore.Qt.Key_Escape:
            self.fechar_projetor()

    def fechar_projetor(self):
        self.projetor_window.close()

    def projetar(self):
        self.projetor_window.show()

    def pesquisar(self):
        pesquisa = self.pesquisaLineEdit.text()
        if pesquisa != '':
            referencia = self.bible.query_one(pesquisa)
            texto_referencia = f"{referencia['text']} ({format_reference(referencia)})"
            self.mainTextEdit.setText(texto_referencia)
            self.projetor_window.textLabel.setText(texto_referencia)
