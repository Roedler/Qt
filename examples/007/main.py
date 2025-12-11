import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from ui_QListWidgetDemo import Ui_MainWindow

class Example_007(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.listWidget = self.ui.listWidget
        self.addButton = self.ui.addButton
        self.lineEdit = self.ui.lineEdit

        self.setConnections()

    @Slot()
    def setConnections(self):
        self.addButton.clicked.connect(self.addButtonClicked)
        self.listWidget.itemClicked.connect(self.listItemClicked)

    @Slot()
    def addButtonClicked(self):
        self.addListItem(self.getInputFieldText())

    @Slot()
    def addListItem(self, string):
        if string != "":
            self.listWidget.addItem(string)
            self.setInputFieldText()

    @Slot()
    def setInputFieldText(self):
        self.lineEdit.setText('')

    @Slot()
    def getInputFieldText(self):
        return self.lineEdit.text()

    @Slot(QListWidgetItem)
    def listItemClicked(self, item):
        print("Item clicked: " + item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Example_007()
    widget.show()
    sys.exit(app.exec())
