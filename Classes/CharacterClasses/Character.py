from Constants import WIN
import Constants


class Character:
    def __init__(self, name, sprite, pos, world):
        self.name = name
        self.sprite = sprite
        self.pos = pos
        self.world = world

    def draw(self, camera_pos):

        tile = Constants.TILES["l"]
        if self.world[self.pos[1]][self.pos[0]] == "l":

            # Grass underneath the leaves
            WIN.blit(Constants.TILES["G"], (self.pos[0] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                                            self.pos[1] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))

            # Player
            WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                                   self.pos[1] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))
            # Changing leaf transparency and drawing it
            tile.set_alpha(200)
            WIN.blit(tile, (self.pos[0] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                            self.pos[1] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))
        else:
            # Return the leaf to normal transparency
            tile.set_alpha(255)
            WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (camera_pos[0] * Constants.SCALE),
                                   self.pos[1] * Constants.SCALE - (camera_pos[1] * Constants.SCALE)))
