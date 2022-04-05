#!/usr/bin/python3
import sys
from Controller import Controller
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    # Create the application.
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_gui()

    sys.exit(app.exec_())
