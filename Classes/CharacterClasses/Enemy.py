from Classes.CharacterClasses.NitzamonUser import *


class Enemy(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, fight_lines, world, fainted):
        super().__init__(name, sprite, pos, nitzamons, world)
        self.fight_lines = fight_lines
        self.fainted = fainted

    def start_fight(self):
        pass

    def enemy_is_dead(self):
        pass
