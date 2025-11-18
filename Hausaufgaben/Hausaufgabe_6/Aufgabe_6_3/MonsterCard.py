from Hausaufgaben.Hausaufgabe_6.Aufgabe_6_3.BasicCard import BasicCard


class MonsterCard(BasicCard):
    """
    Represents a monster card with combat statistics.
    Inherits title and subtitle from BasicCard.
    """
    def __init__(self, title, subtitle, healthPoints, attackValue, defenseValue, damageValue, armorValue, pixmap=None, key=None):
        super().__init__(title, subtitle, key, pixmap)
        self.__healthPoints = healthPoints
        self.__attackValue = attackValue
        self.__defenseValue = defenseValue
        self.__damageValue = damageValue
        self.__armorValue = armorValue

    def getHealthPoints(self):
        return self.__healthPoints

    def getAttackValue(self):
        return self.__attackValue

    def getDefenseValue(self):
        return self.__defenseValue

    def getDamageValue(self):
        return self.__damageValue

    def getArmorValue(self):
        return self.__armorValue

    def toString(self):
        """
        Returns a formatted string of all card details,
        including the inherited base details and combat stats.
        """
        baseString = super().toString()

        statsString = (
            f"\n--- Combat Stats ---\n"
            f"Health Points (HP): {self.getHealthPoints()}\n"
            f"Attack (ATT): {self.getAttackValue()}\n"
            f"Defense (DEF): {self.getDefenseValue()}\n"
            f"Damage (DMG): {self.getDamageValue()}\n"
            f"Armor (ARM): {self.getArmorValue()}"
        )

        return baseString + statsString
