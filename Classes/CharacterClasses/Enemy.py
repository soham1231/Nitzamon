from Classes.CharacterClasses.NitzamonUser import *


class Enemy(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, fight_lines, world):
        super().__init__(name, sprite, pos, nitzamons, world)
        self.fight_lines = fight_lines
