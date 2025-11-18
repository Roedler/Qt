import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap

imgName = 'lorem_picsum'
imgEnding = 'jpg'
imgFileName = imgName + '.' + imgEnding

app = QApplication(sys.argv)
pixmap = QPixmap(imgFileName)
label = QLabel()
label.setPixmap(pixmap)
label.adjustSize()
label.show()
app.exec()
