import Character
class NPC(Character):
    def __init__(self, name, sprite, quests, small_talk):
        super(self, name, sprite)
        self.quests = quests
        self.small_talk = small_talk