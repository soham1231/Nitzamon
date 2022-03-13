from Constants import WIN
import Constants


class Character:
    def __init__(self, name, sprite, pos, world):
        self.name = name
        self.sprite = sprite
        self.pos = pos
        self.world = world

    def draw(self, camera_pos):

        if self.world[self.pos[1]][self.pos[0]] == "l":
            # WIN.blit(self.sprite, (self.pos[1] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
            #                        self.pos[0] * Constants.SCALE - (camera_pos[1] * Constants.SCALE))) # Should use that if we make leaves transparent
            tile = Constants.TILES[self.world[self.pos[0]][self.pos[1]]]
            WIN.blit(tile, (self.pos[1] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                            self.pos[0] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))
        else:
            WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                                   self.pos[1] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))
