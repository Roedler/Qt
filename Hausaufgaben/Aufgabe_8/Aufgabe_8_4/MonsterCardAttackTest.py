from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from Hausaufgaben.Aufgabe_8.Aufgabe_8_4.MonsterCard import MonsterCard
from Hausaufgaben.Aufgabe_8.Aufgabe_8_4.ui_MonsterCardAttackTest import Ui_DuelWindow


class MonsterCardAttackTest(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_DuelWindow()
        self.ui.setupUi(self)
        self.card_left = MonsterCard("Der Stille Jäger")
        self.card_right = MonsterCard("Astrales Echo")

        self.stats_left = {
            'hp': self.ui.lbl_HPL,
            'def': self.ui.lbl_DefL,
            'atk': self.ui.lbl_AtkL
        }
        self.stats_right = {
            'hp': self.ui.lbl_HPR,
            'def': self.ui.lbl_DefR,
            'atk': self.ui.lbl_AtkR
        }

        self.current_attacker = self.card_left

        self._initialize_stats()
        self.ui.btn_Attack.clicked.connect(self._handle_attack)


    def _initialize_stats(self):
        self.stats_left['hp'].setText(str(self.card_left.current_hp))
        self.stats_left['def'].setText(str(self.card_left.defense))
        self.stats_left['atk'].setText(str(self.card_left.attack))

        self.stats_right['hp'].setText(str(self.card_right.current_hp))
        self.stats_right['def'].setText(str(self.card_right.defense))
        self.stats_right['atk'].setText(str(self.card_right.attack))

    def _update_ui_health(self):
        self.stats_left['hp'].setText(str(self.card_left.current_hp))
        if self.card_left.current_hp <= 0:
            self.ui.leftCard.setStyleSheet(self.ui.leftCard.styleSheet() + "border: 5px solid red;")
            self.ui.lbl_HPL.setStyleSheet(self.ui.lbl_HPL.styleSheet() + "background-color: darkred;")
            self.ui.lbl_HPL.setText("X")
            print(f"{self.card_left.name} ist besiegt!")

        self.stats_right['hp'].setText(str(self.card_right.current_hp))
        if self.card_right.current_hp <= 0:
            self.ui.rightCard.setStyleSheet(self.ui.rightCard.styleSheet() + "border: 5px solid red;")
            self.ui.lbl_HPR.setStyleSheet(self.ui.lbl_HPR.styleSheet() + "background-color: darkred;")
            self.ui.lbl_HPR.setText("X")
            print(f"{self.card_right.name} ist besiegt!")

    @Slot()
    def _handle_attack(self):
        if self.card_left.current_hp <= 0 or self.card_right.current_hp <= 0:
            print("\nDas Duell ist beendet. Starten Sie das Programm neu.")
            self.ui.btn_Attack.setEnabled(False)
            return

        if self.current_attacker == self.card_left:
            attacker = self.card_left
            target = self.card_right
        else:
            attacker = self.card_right
            target = self.card_left

        print("-" * 30)
        print(f"Zug: {attacker.name} (AP: {attacker.attack}) greift {target.name} (RP: {target.defense}) an.")

        # 1. Attacker attacks card
        damage_to_target = target.calculate_damage_taken(attacker.attack)
        print(f"-> {target.name} erleidet {damage_to_target} Netto-Schaden. HP: {target.current_hp}")

        # 2. Attacked card attacks back
        damage_to_attacker = attacker.calculate_damage_taken(target.attack)
        print(f"-> {attacker.name} erleidet {damage_to_attacker} Netto-Schaden. HP: {attacker.current_hp}")

        self._update_ui_health()
        self.current_attacker = target
        self.ui.btn_Attack.setText(f"ANGREIFEN (Nächster Zug: {self.current_attacker.name})")
