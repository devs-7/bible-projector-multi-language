import sys
# import update_windows

from PyQt5.QtWidgets import QApplication
from ui.main.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    app.exec()
