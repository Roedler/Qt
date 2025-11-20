import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot

@Slot()
def sayHello():
    print("Hello world")

app = QApplication(sys.argv)
button = QPushButton("Click me")
button.clicked.connect(sayHello)
button.show()
app.exec()
