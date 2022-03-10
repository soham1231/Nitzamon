from Classes.CharacterClasses.Character import *


class NitzamonUser(Character):
    def __init__(self, name, sprite, pos, nitzamons):
        super().__init__(name, sprite, pos)
        self.nitzamons = nitzamons
