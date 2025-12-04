import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_Aufgabe_7 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionSpeichern.triggered.connect(self.save)

    @Slot()
    def save(self):
        print("save")

    @Slot(int)
    def on_horizontalSlider_valueChanged(self, value=0):
        if value < 3:
            color = "blue"
        elif value > 20:
            color = "red"
        else:
            color = "grey"

        cssstr = """
        QSlider::groove:horizontal {
            border: 2px solid #999999;
            height: 10px;
            background: grey;
            margin: 2px 0;
        }
        
        QSlider::handle:horizontal {
            background: """ + color + """;
            border: 10px solid black;
            width: 40px;
            height: 40px;
            margin: -25px 0;
            border-radius: 25px;
        }
        """

        self.ui.horizontalSlider.setStyleSheet(cssstr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    widget.show()
    sys.exit(app.exec())
