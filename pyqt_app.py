#!/usr/bin/env python3

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QMainWindow,
    QPushButton,
    QWidget,
    )

'''
Sample PyQt6 GUI to be reused and modified in other projects
'''

class dlgWindow(QDialog):
    def __init__(self):
        super().__init__()
    
        buttons = (
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Close
            )
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Window title
        self.setWindowTitle("PyQt6 GUI")

        # Window size
        self.windowW = 420
        self.windowH = 240
        self.setMinimumSize(self.windowW, self.windowH)

        # Create submit button
        submit_button = QPushButton("Send")
        submit_button.setCheckable(True)
        submit_button.clicked.connect(self.was_clicked)
        # Create label
        label = QLabel("Hey!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Set layout
        layout = QGridLayout()
        # layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(label, 0, 0)
        layout.addWidget(submit_button, 1, 0)

        # Create widget
        widget = QWidget()
        widget.setLayout(layout)

        # Set central widget
        self.setCentralWidget(widget)

    def was_clicked(self):
        print("Button clicked")
        dlg = dlgWindow()
        dlg.exec()
        # dlg = QDialog(self)
        # dlg.setWindowTitle("Dialog Window")
        # dlg.setMinimumSize(self.windowW // 2, self.windowH // 2)
        # dlg.exec()


app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()   # Create the window
window.show()   # Show window
app.exec()  # Start the loop
