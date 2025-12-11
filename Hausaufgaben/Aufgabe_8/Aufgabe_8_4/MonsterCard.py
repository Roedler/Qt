import random

class MonsterCard:
    def __init__(self, name: str):
        self.name = name
        self.max_hp = random.randint(5, 15)
        self.current_hp = self.max_hp
        self.attack = random.randint(3, 10)
        self.defense = random.randint(1, 5)

    def calculate_damage_taken(self, incoming_attack: int) -> int:
        damage = max(0, incoming_attack - self.defense)
        self.current_hp = max(0, self.current_hp - damage)
        return damage
