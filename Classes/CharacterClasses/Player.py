from NitzamonUser import *
import WorldFunctions
import Constants
from Constants import WIN
import math
import pygame


class Player(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons=0, nitzamon_bag=0, active_quests=0):
        super().__init__(name, sprite, pos, nitzamons)
        self.nitzamon_bag = nitzamon_bag
        self.active_quests = active_quests
        self.camera_pos = [0, 0]

    def camera(self):
        world = WorldFunctions.read_world("World1")
        max_camera_y = int(len(world) - (Constants.Y / Constants.SCALE))
        max_camera_x = int(len(world) - (Constants.X / Constants.SCALE))
        camera_x = self.pos[0] - math.ceil(round(Constants.X / Constants.SCALE / 2))
        camera_y = self.pos[1] - math.ceil(round(Constants.Y / Constants.SCALE / 2))
        if max_camera_y >= camera_y >= 0:
            self.camera_pos[1] = camera_y
        elif camera_y < 0:
            self.camera_pos[1] = 0
        else:
            self.camera_pos[1] = max_camera_y

        if max_camera_x >= camera_x >= 0:
            self.camera_pos[0] = camera_x
        elif camera_x < 0:
            self.camera_pos[0] = 0
        else:
            self.camera_pos[0] = max_camera_x

    def draw_player(self):
        WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (self.camera_pos[0] * Constants.SCALE),
                               self.pos[1] * Constants.SCALE - (self.camera_pos[1] * Constants.SCALE)))
        
    def check_in_bounds(self, pos):
        world = WorldFunctions.read_world("World1")
        if pos[0] >= len(world):
            return False
        if pos[0] < 0:
            return False
        if pos[1] >= len(world):
            return False
        if pos[1] < 0:
            return False
        return True

    def move(self, keys):
        if keys[pygame.K_a] and self.check_in_bounds([self.pos[0] - 1, self.pos[1]]):  # Left
            self.pos[0] -= 1
        if keys[pygame.K_d] and self.check_in_bounds([self.pos[0] + 1, self.pos[1]]):  # Right
            self.pos[0] += 1
        if keys[pygame.K_w] and self.check_in_bounds([self.pos[0], self.pos[1] - 1]):  # Up
            self.pos[1] -= 1
        if keys[pygame.K_s] and self.check_in_bounds([self.pos[0], self.pos[1] + 1]):  # Down
            self.pos[1] += 1