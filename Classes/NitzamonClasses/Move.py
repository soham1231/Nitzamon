class Move:
    def __init__(self, element, dmg, name, sound):
        self.element = element
        self.dmg = dmg
        self.name = name
        self.sound = sound

    def get_effectiveness(self, enemy_type):
        if self.element == "water":
            if enemy_type == "water" or enemy_type == "grass":
                return "Not very effective"
            if enemy_type == "fire":
                return "Super effective"
            else:
                return "Effective"
        if self.element == "earth":
            if enemy_type == "fire" or enemy_type == "earth":
                return "Not very effective"
            if enemy_type == "water":
                return "Super effective"
            else:
                return "Effective"
        if self.element == "fire":
            if enemy_type == "water" or enemy_type == "fire":
                return "Not very effective"
            if enemy_type == "earth":
                return "Super effective"
            else:
                return "Effective"
