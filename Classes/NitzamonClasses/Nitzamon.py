import random
import pygame
import Constants
from time import sleep


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
        self.dmg += random.randint(lvl_num + 2, lvl_num + 10)
        self.max_hp += random.randint(lvl_num + 5, lvl_num + 15)
        self.hp = self.max_hp
        self.spd += lvl_num
        if self.lvl >= 10 and not self.evolved:
            self.evolved = True
            if self.name != Constants.GEM_TRIO and self.name != Constants.NITZAPHONE and self.name != Constants.MASMERION:
                return False
            return True
        return False

    def evolve(self):
        if self.name == Constants.NITZAPHONE:
            self.name = "nitzatop"
        elif self.name == Constants.GEM_TRIO:
            self.name = "Gem Army"
        elif self.name == Constants.MASMERION:
            self.name = "Agent Patish"
        size = Constants.X // 4
        old_sprite = pygame.transform.scale(self.sprite, (size, size))
        self.sprite = pygame.image.load(f"Assets\\Nitzamons\\{self.name}.png")
        new_sprite = pygame.transform.scale(self.sprite, (size, size))

        clock = pygame.time.Clock()
        for i in range(360):
            clock.tick(1000)
            Constants.WIN.fill(Constants.GREY)
            if i % 2 == 0 and i <= 255:
                old_sprite.set_alpha(255 - i)
            Constants.WIN.blit(pygame.transform.rotate(old_sprite, i), (Constants.X//2 - new_sprite.get_width() // 2, Constants.Y//2 - old_sprite.get_height() + 15))
            pygame.display.update()

        Constants.WIN.fill(Constants.GREY)
        Constants.WIN.blit(new_sprite, (Constants.X // 2 - new_sprite.get_width() // 2, Constants.Y // 2 - new_sprite.get_height() + 15))
        pygame.display.update()
        sleep(2)
