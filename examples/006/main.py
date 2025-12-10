import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from ui_example_006 import Ui_MainWindow

class Example_006(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Example_006()
    widget.show()
    sys.exit(app.exec())
