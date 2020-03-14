import sys
import helper.bible as bible

from PyQt5.QtWidgets import QApplication
from ui.main_view.main_view import MainView

print(bible.query_one('mt 11 28'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    app.exec()
