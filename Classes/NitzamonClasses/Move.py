

class Move:

    def __init__(self, move_element, move_dmg, name):
        self.move_element = move_element
        self.move_dmg = move_dmg
        self.name = name

    def get_effectiveness(self, enemy_type):
        if self.move_element == "water":
            if enemy_type == "water" or enemy_type == "grass":
                return "Not very effective"
            if enemy_type == "fire":
                return "Super effective"
            else:
                return "Effective"
        if self.move_element == "earth":
            if enemy_type == "fire" or enemy_type == "earth":
                return "Not very effective"
            if enemy_type == "water":
                return "Super effective"
            else:
                return "Effective"
        if self.move_element == "fire":
            if enemy_type == "water" or enemy_type == "fire":
                return "Not very effective"
            if enemy_type == "earth":
                return "Super effective"
            else:
                return "Effective"
