from ui.main.window import *
from PyQt5.QtWidgets import QMainWindow
from model.bible import Bible, format_reference


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.bible = Bible()

        self.pesquisarButton.clicked.connect(self.pesquisar)
        self.projetarButton.clicked.connect(self.projetar)

    def projetar(self):
        pass

    def pesquisar(self):
        pesquisa = self.pesquisaLineEdit.text()
        if pesquisa != '':
            referencia = self.bible.query_one(pesquisa)
            self.mainTextEdit.setText(f"{referencia['text']} ({format_reference(referencia)})")
