

class Nitzamon:

    def __init__(self, name, lvl, hp, max_hp, dmg, spd, sprite, element, list_of_moves, entrance_sound, death_sound):
        self.name = name
        self.element = element
        self.dmg = dmg
        self.hp = hp
        self.max_hp = max_hp
        self.spd = spd
        self.sprite = sprite
        self.list_of_moves = list_of_moves
        self.lvl = lvl
        self.entrance_sound = entrance_sound
        self.death_sound = death_sound
