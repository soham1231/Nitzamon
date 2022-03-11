from Classes.CharacterClasses.NitzamonUser import *


class Enemy(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, fight_lines):
        super().__init__(name, sprite, pos, nitzamons)
        self.fight_lines = fight_lines
