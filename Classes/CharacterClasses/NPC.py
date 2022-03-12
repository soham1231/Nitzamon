from Character import *


class NPC(Character):
    def __init__(self, name, sprite, pos, quests, small_talk, world):
        super().__init__(name, sprite, pos, world)
        self.quests = quests
        self.small_talk = small_talk
