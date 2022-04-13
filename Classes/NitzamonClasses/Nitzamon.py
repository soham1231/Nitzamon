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
        self.evolved = lvl >= 15
        self.entrance_sound = pygame.mixer.Sound(f"Assets\\Sounds\\Fight Entrance\\{name}.mp3")
        self.death_sound = pygame.mixer.Sound(f"Assets\\Sounds\\Death\\{name}.mp3")

        self.entrance_sound.set_volume(0.1)
        self.death_sound.set_volume(0.1)

    def level_up(self, lvl_num):
        self.lvl += lvl_num
        self.dmg += lvl_num + 2
        self.max_hp += lvl_num + 2
        self.hp = self.max_hp
        self.spd += lvl_num
        if self.lvl >= 15 and not self.evolved:
            self.evolved = True
            if self.name != Constants.NITZAPHONE and self.name != Constants.GEM_TRIO and self.name != Constants.MASMERION:
                return False
            if self.name == Constants.NITZAPHONE:
                self.name = "nitzatop"
            elif self.name == Constants.GEM_TRIO:
                self.name = "Gem Army"
            elif self.name == Constants.MASMERION:
                self.name = "Agent Patish"
            self.sprite = pygame.image.load(f"Assets\\Nitzamons\\{self.name}.png")
            return True
        return False