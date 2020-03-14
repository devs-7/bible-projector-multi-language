import sys
import update_views

from PyQt5.QtWidgets import QApplication
from ui.main.main_window import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    app.exec()
