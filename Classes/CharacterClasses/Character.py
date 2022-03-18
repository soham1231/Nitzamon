from Constants import WIN
import Constants


class Character:
    def __init__(self, name, sprite, pos, world):
        self.name = name
        self.sprite = sprite
        self.pos = pos
        self.world = world
