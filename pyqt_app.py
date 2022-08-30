#!/usr/bin/env python3

'''
Sample PyQt6 GUI to be reused and modified in other projects
'''

from PyQt6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)


if __name__=="__main__":

    # Create the window
    window = QWidget()

    # Show the window
    window.show()

    # Start the loop
    app.exec()
