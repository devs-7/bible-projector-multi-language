from ui.main_view.view import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QKeyEvent
from model.bible import Bible, format_reference



class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.bible = Bible()

        self.pesquisarButton.clicked.connect(self.pesquisar)
        self.pesquisaLineEdit.keyPressEvent = self.pesquisa_line_edit_key_press

    def pesquisa_line_edit_key_press(self, e: QKeyEvent):
        print(e.text())

    def pesquisar(self):
        pesquisa = self.pesquisaLineEdit.text()
        if pesquisa != '':
            referencia = self.bible.query_one(pesquisa)
            self.mainTextEdit.setText(f"{referencia['text']} ({format_reference(referencia)})")
