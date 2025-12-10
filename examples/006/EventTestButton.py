import sys

from PySide6.QtWidgets import QPushButton

class EventTestButton(QPushButton):
    _click_counter = 0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self.inc_click_counter)

    def inc_click_counter(self):
        self._click_counter += 1
        print('Click counter: ', self._click_counter)
