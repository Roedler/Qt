import random
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PySide6.QtCore import Slot, Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ["Hallo", "Hello", "Salut", "Salam", "Ola"]
        self.button = QPushButton("Click me!")
        self.label = QLabel(self.hello[0], alignment=Qt.AlignCenter)
        self.le = QLineEdit()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)
        self.le.returnPressed.connect(self.magic)
        self.le.textChanged.connect(self.magic)


    @Slot()
    def magic(self):
        self.label.setText(self.hello[random.randint(0, len(self.hello) - 1)] + " " + self.le.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    app.exec()
