# -*- coding: utf-8 -*-
# contacts/main.py

""" This module provides Contacts app """

import sys

from PyQt5.QtWidgets import QApplication

from .views import Window
def main():
    """ Contacts main """
    #Here we create the app
    app = QApplication(sys.argv)
    #We create the main window
    win = Window()
    win.show()
    #Run the event loop
    sys.exit(app.exec())
