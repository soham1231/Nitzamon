import Character
class NitzamonUser(Character):
    def __init__(self, name, sprite, nitzamons, num_of_nitzamons):
        super(self, name, sprite)
        self.nitzamons = nitzamons
        self.num_of_nitzamons = num_of_nitzamons