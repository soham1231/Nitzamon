from Constants import WIN
import Constants


class Character:
    def __init__(self, name, sprite, pos, world):
        self.name = name
        self.sprite = sprite
        self.pos = pos
        self.world = world

    def draw(self, camera_pos):
        WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                               self.pos[1] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))
