from Classes.CharacterClasses.NitzamonUser import *
from Worlds import WorldFunctions
import Constants
from Constants import WIN
import math
import pygame


class Player(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, nitzamon_bag, active_quests):
        super().__init__(name, sprite, pos, nitzamons)
        self.nitzamon_bag = nitzamon_bag
        self.active_quests = active_quests
        self.camera_pos = [0, 0]

    # Making the camera that follows the player
    def camera(self):
        world = WorldFunctions.read_world(Constants.WORLD1_PATH)
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


    # Only use it in the movement method
    def check_collisions(self, pos):
        world = WorldFunctions.read_world(Constants.WORLD1_PATH)

        if pos[0] >= len(world) - 1:
            return False

        if pos[0] < 0:
            return False

        if pos[1] >= len(world) - 1:
            return False

        if pos[1] < 0:
            return False

        if world[pos[0]][pos[1]] not in Constants.WALKABLE_TILES:
            return False

        return True

    def move(self, keys):
        if (keys[pygame.K_w] or keys[pygame.K_s]) and (keys[pygame.K_a] or keys[pygame.K_d]):  # Reducing fps when player moves diagonally
            if Constants.fps == Constants.FPS:
                Constants.fps /= 2
        else:
            Constants.fps = Constants.FPS

        if keys[pygame.K_a] and self.check_collisions([self.pos[0] - 1, self.pos[1]]):  # Left
            self.pos[0] -= 1

        if keys[pygame.K_d] and self.check_collisions([self.pos[0] + 1, self.pos[1]]):  # Right
            self.pos[0] += 1

        if keys[pygame.K_w] and self.check_collisions([self.pos[0], self.pos[1] - 1]):  # Up
            self.pos[1] -= 1

        if keys[pygame.K_s] and self.check_collisions([self.pos[0], self.pos[1] + 1]):  # Down
            self.pos[1] += 1
