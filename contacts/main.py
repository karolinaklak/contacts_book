# -*- coding: utf-8 -*-
# contacts/main.py

""" This module provides Contacts app """

import sys

from .database import createConnection
from PyQt5.QtWidgets import QApplication

from .views import Window
def main():
    """ Contacts main """
    #Here we create the app
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    #We create the main window
    win = Window()
    win.show()
    #Run the event loop
    sys.exit(app.exec())
