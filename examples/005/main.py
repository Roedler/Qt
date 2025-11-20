import sys

from PySide6.QtWidgets import QWidget, QApplication
from compiled.myFirstUi import Ui_Form

class MyFirstUi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyFirstUi()
    widget.show()
    sys.exit(app.exec())
