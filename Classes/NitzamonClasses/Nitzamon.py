import random
import pygame
import Constants


class Nitzamon:

    def __init__(self, name, lvl, list_of_moves):
        self.name = name
        self.element = Constants.NITZAMON_ELEMENTS_DICT[name]
        self.dmg = lvl + random.randint(lvl, lvl + 10)
        self.hp = lvl * 5
        self.max_hp = self.hp
        self.spd = lvl + random.randint(lvl, lvl + 5)
        self.sprite = pygame.image.load(f"Assets\\Nitzamons\\{name}.png")
        self.list_of_moves = list_of_moves
        self.lvl = lvl
        self.entrance_sound = pygame.mixer.Sound(f"Assets\\Sounds\\Fight Entrance\\{name}.mp3")
        self.death_sound = pygame.mixer.Sound(f"Assets\\Sounds\\Death\\{name}.mp3")

        self.entrance_sound.set_volume(0.1)
        self.death_sound.set_volume(0.1)

    def level_up(self, lvlNum):
        self.lvl += lvlNum
        self.dmg += lvlNum + 2
        self.max_hp += lvlNum + 2
        self.hp = self.max_hp
        self.spd += lvlNum
