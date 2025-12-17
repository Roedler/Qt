import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem

from MonsterCard import MonsterCard
from ui_QListWidgetDemo import Ui_MainWindow

class Aufgabe_9_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.showCardDeck()

    def showCardDeck(self):
        media_path = os.path.join(os.path.dirname(__file__), "!Media")
        files = [f for f in os.listdir(media_path) if f.endswith(".png")]

        for file in files:
            display_name = file.replace(".png", "")
            card_widget = MonsterCard(display_name, file)
            item = QListWidgetItem(self.ui.listWidget)
            item.setSizeHint(card_widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, card_widget)

        self.ui.listWidget.setSpacing(10)
        self.ui.listWidget.setViewMode(self.ui.listWidget.ViewMode.IconMode)
        self.ui.listWidget.setResizeMode(self.ui.listWidget.ResizeMode.Adjust)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Aufgabe_9_2()
    widget.show()
    sys.exit(app.exec())
