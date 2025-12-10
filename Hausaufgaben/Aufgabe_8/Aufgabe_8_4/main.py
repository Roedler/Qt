import sys
from PySide6.QtWidgets import QApplication

from Hausaufgaben.Aufgabe_8.Aufgabe_8_4.MonsterCardAttackTest import MonsterCardAttackTest

app = QApplication(sys.argv)
widget = MonsterCardAttackTest()
widget.show()
sys.exit(app.exec())
