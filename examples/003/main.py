import random
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PySide6.QtCore import Slot, Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ["Hallo", "Hello", "Salut", "Salam", "Ola"]

        self.button = QPushButton("Click me!")
        self.quitButton = QPushButton("Quit")

        self.label = QLabel(self.hello[0], alignment=Qt.AlignCenter)
        self.le = QLineEdit()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.quitButton)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.changeGreeting)
        self.quitButton.clicked.connect(self.close)
        self.le.returnPressed.connect(self.changeName)
        self.le.textChanged.connect(self.changeName)

        self.greeting = self.hello[0]
        self.name = ""

    @Slot()
    def changeGreeting(self):
        self.greeting = random.choice(self.hello)
        self.label.setText(self.greeting + " " + self.name)

    @Slot()
    def changeName(self):
        self.name = self.le.text()
        self.label.setText(self.greeting + " " + self.name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    app.exec()
