from Classes.CharacterClasses.Character import Character
from Constants import *
import pygame


class NPC(Character):
    def __init__(self, name, sprite, pos, quests, small_talk, world):
        super().__init__(name, sprite, pos, world)
        self.quests = quests
        self.small_talk = small_talk
        #npc_list.append(self)  # npc_list is a list that contains all npcs, used for the npc functions

    def talk(self, player):
        if ((player.pos[0] == self.pos[0] - 1) and (player.pos[1] == self.pos[1])) or \
                ((player.pos[0] == self.pos[0]) and (player.pos[1] == self.pos[1]) + 1) or \
                ((player.pos[0] == self.pos[0] + 1) and (player.pos[1] == self.pos[1])) or \
                ((player.pos[0] == self.pos[0]) and (player.pos[1] == self.pos[1] - 1)):
            pygame.draw.rect(WIN, BLACK, pygame.Rect((0, (3 * Y / 4)), (X, (3 * Y / 4))))
            font = pygame.font.SysFont("Comic Sans MS", 25)
            npc_sprite = pygame.transform.scale(self.sprite, (X / 4, Y / 4m))
            text = font.render(self.small_talk[0].text, True, (255, 255, 255))
            WIN.blit(npc_sprite, (X - npc_sprite.get_width(), (3 * Y / 4) + 10))
            WIN.blit(text, (10, (3 * Y / 4) + 10))
