from Classes.CharacterClasses.Character import *
from Classes.CharacterClasses.Player import *
from Constants import *
import pygame
class NPC(Character):
    def __init__(self, name, sprite, pos, quests, small_talk, world):
        super().__init__(name, sprite, pos, world)
        self.quests = quests
        self.small_talk = small_talk

    def talk(self, player , dialogue):
        if ((player.pos[0] == self.pos[0] - 1) and (player.pos[1] == self.pos[1])):
            pass
        # pygame.draw.rect(WIN, BLACK, pygame.Rect((0, (3 * Y / 4)), (X, (3 * Y / 4))))
        # font = pygame.font.SysFont("Comic Sans MS", 10)
        # text = font.render(dialogue.getText(), True, (255, 255, 255))

