from Classes.CharacterClasses.Character import *


class NitzamonUser(Character):
    def __init__(self, name, sprite, pos, nitzamons, world):
        super().__init__(name, sprite, pos, world)
        self.nitzamons = nitzamons
        self.equipped_nitzamon = nitzamons[0]
