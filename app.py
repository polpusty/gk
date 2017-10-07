# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication

from window import MainWindow, Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
