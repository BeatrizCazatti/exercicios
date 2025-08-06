from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        #self.resize(300, 300)
        self.setWindowTitle("Tela de Login")
        self.setContentsMargins(20, 20, 20, 20)

        layout = QGridLayout()
        self.setLayout(layout)

        self.label1 = QLabel("Username: ")
        layout.addWidget(self.label1, 0, 0)

        self.label2 = QLabel("Password: ")
        layout.addWidget(self.label2, 1, 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 0, 1)

        self.input2 = QLineEdit()
        layout.addWidget(self.input2, 1, 1)

        self.button = QPushButton("Entrar")
        self.button.setFixedWidth(60)
        self.button.clicked.connect(self.display)
        layout.addWidget(self.button, 2, 1, Qt.AlignmentFlag.AlignRight)

    def display(self):
        print(self.input1.text())
        print(self.input2.text())

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())