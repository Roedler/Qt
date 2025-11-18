import uuid
from PySide6 import QtCore
from PySide6.QtGui import QPixmap

class BasicCard(QtCore.QObject):
    def __init__(self, title, subtitle, key=None, pixmap=None):
        super().__init__()
        self.__key = key if key is not None else str(uuid.uuid4())
        self.__title = title
        self.__subtitle = subtitle
        if isinstance(pixmap, QPixmap):
            self.__pixmap = pixmap
        else:
            self.__pixmap = None

    def getKey(self):
        return self.__key

    def getPixmap(self):
        return self.__pixmap

    def getTitle(self):
        return self.__title

    def getSubtitle(self):
        return self.__subtitle

    def toString(self):
        pixmap_info = "Yes" if self.__pixmap is not None else "No"
        return (f"Key: {self.getKey()}"
                f"\nTitle: {self.getTitle()}"
                f"\nSubtitle: {self.getSubtitle()}"
                f"\nImage attached: {pixmap_info}")
