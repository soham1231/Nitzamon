import NitzamonUser

class Player(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, nitzamon_bag, active_quests):
        super.__init__(self, name, sprite, pos, nitzamons)
        self.nitzamon_bag = nitzamon_bag
        self.active_quests = active_quests