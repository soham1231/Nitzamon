import Constants


class Move:
    def __init__(self, element, dmg, name, sound):
        self.element = element
        self.dmg = dmg
        self.name = name
        self.sound = sound
        self.sound.set_volume(0.1)

    def get_effectiveness(self, enemy_type):
        if self.element == Constants.WATER:
            if enemy_type == Constants.WATER or enemy_type == Constants.EARTH:
                return "Not very effective"
            if enemy_type == Constants.FIRE:
                return "Super effective"
            else:
                return "Effective"
        if self.element == Constants.EARTH:
            if enemy_type == Constants.FIRE or enemy_type == Constants.EARTH:
                return "Not very effective"
            if enemy_type == Constants.WATER:
                return "Super effective"
            else:
                return "Effective"
        if self.element == Constants.FIRE:
            if enemy_type == Constants.WATER or enemy_type == Constants.FIRE:
                return "Not very effective"
            if enemy_type == Constants.EARTH:
                return "Super effective"
            else:
                return "Effective"
        return "Effective"