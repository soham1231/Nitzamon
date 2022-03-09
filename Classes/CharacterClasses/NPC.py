from Character import *


class NPC(Character):
    def __init__(self, name, sprite, pos, quests, small_talk):
        super().__init__(name, sprite, pos)
        self.quests = quests
        self.small_talk = small_talk
