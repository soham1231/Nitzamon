import pygame
import Constants
from Classes.CharacterClasses.NitzamonUser import *


class Enemy(NitzamonUser):
    def __init__(self, name, sprite, pfp, pos, nitzamons, world, fight_talk):
        super().__init__(name, sprite, pos, nitzamons, world)
        self.fight_talk = fight_talk
        self.pfp = pfp


    def start_fight(self):
        pass

    def enemy_is_dead(self):
        pass

    def talk(self, player):
        if ((player.pos[0] == self.pos[0] - 1) and (player.pos[1] == self.pos[1])) or \
                ((player.pos[0] == self.pos[0]) and (player.pos[1] == self.pos[1]) + 1) or \
                ((player.pos[0] == self.pos[0] + 1) and (player.pos[1] == self.pos[1])) or \
                ((player.pos[0] == self.pos[0]) and (player.pos[1] == self.pos[1] - 1)):
            pygame.draw.rect(WIN, Constants.BLACK, pygame.Rect((0, (3 * Constants.Y / 4)), (Constants.X, (3 * Constants.Y / 4))))
            font = pygame.font.SysFont("Comic Sans MS", 25)
            text = font.render(self.fight_talk, True, (255, 255, 255))
            WIN.blit(self.pfp, (Constants.X - self.pfp.get_width(), (3 * Constants.Y / 4)))
            WIN.blit(text, (10, (3 * Constants.Y / 4) + 10))
            #HELLO