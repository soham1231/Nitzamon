from Constants import WIN
import Constants


class Character:
    def __init__(self, name, sprite, pos):
        self.name = name
        self.sprite = sprite
        self.pos = pos

    def draw(self, p):
        WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (p.camera_pos[0] * Constants.SCALE),
                               self.pos[1] * Constants.SCALE - (p.camera_pos[1] * Constants.SCALE)))
