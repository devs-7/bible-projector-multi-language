import sys

from PyQt5.QtWidgets import QApplication
from ui.main_view.main_view import MainView
from model.bible import Bible

bible = Bible('NTLH')
x = bible.query_one('gn 1 1')
print(x)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    app.exec()
