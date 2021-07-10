import sys

from PyQt5.QtWidgets import QApplication

from src.ui.main.main_window import MainWindow

# import update_windows


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    app.exec()
