from Classes.CharacterClasses.NitzamonUser import *


class Enemy(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, world, fainted):
        super().__init__(name, sprite, pos, nitzamons, world)
        self.fainted = fainted

    def start_fight(self):
        pass

    def enemy_is_dead(self):
        pass
