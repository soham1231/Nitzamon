from Classes.CharacterClasses.NitzamonUser import *
import Constants
import math
import pygame


class Player(NitzamonUser):
    def __init__(self, name, sprite, pos, nitzamons, nitzamon_bag, active_quests, world, nitzaballs):
        super().__init__(name, sprite, pos, nitzamons, world)
        self.nitzamon_bag = nitzamons + nitzamon_bag
        self.active_quests = active_quests
        self.camera_pos = [0, 0]
        self.nitzaballs = nitzaballs

    # Just a temporary function that heals all the nitzamons in the player's inventory
    def heal_nitzamons(self):
        for nitzamon in self.nitzamon_bag:
            nitzamon.hp = nitzamon.max_hp

    # Checks if nitzaball is already in nitzaball dict, if it is add the amount, if not, put it in
    def add_nitzaballs(self, nitzaball, amount):
        if nitzaball in self.nitzaballs.keys():
            self.nitzaballs[nitzaball] += amount
        else:
            self.nitzaballs[nitzaball] = amount

    # Making the camera that follows the player
    def camera(self):
        max_camera_y = int(len(self.world) - (Constants.Y / Constants.SCALE))
        max_camera_x = int(len(self.world) - (Constants.X / Constants.SCALE))
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
    def check_collisions(self, direction):

        if direction == "r":
            if self.pos[0] + 1 >= len(self.world) - 1:
                return False
            if self.world[self.pos[1]][self.pos[0] + 1] not in Constants.WALKABLE_TILES:
                return False

        if direction == "l":
            if self.pos[0] - 1 < 0:
                return False
            if self.world[self.pos[1]][self.pos[0] - 1] not in Constants.WALKABLE_TILES:
                return False

        if direction == "d":
            if self.pos[1] + 1 >= len(self.world) - 1:
                return False
            if self.world[self.pos[1] + 1][self.pos[0]] not in Constants.WALKABLE_TILES:
                return False

        if direction == "u":
            if self.pos[1] - 1 < 0:
                return False
            if self.world[self.pos[1] - 1][self.pos[0]] not in Constants.WALKABLE_TILES:
                return False

        return True

    def move(self, keys):
        if (keys[pygame.K_w] or keys[pygame.K_s]) and (keys[pygame.K_a] or keys[pygame.K_d]):  # Reducing fps when player moves diagonally
            if Constants.fps == Constants.FPS:
                Constants.fps = int(Constants.FPS / 2)
        else:
            Constants.fps = Constants.FPS

        if keys[pygame.K_a] and self.check_collisions("l"):  # Left
            self.pos[0] -= 1

        if keys[pygame.K_d] and self.check_collisions("r"):  # Right
            self.pos[0] += 1

        if keys[pygame.K_w] and self.check_collisions("u"):  # Up
            self.pos[1] -= 1

        if keys[pygame.K_s] and self.check_collisions("d"):  # Down
            self.pos[1] += 1

    # def draw(self):
    #
    #     tile = Constants.TILES["l"]
    #     if self.world[self.pos[1]][self.pos[0]] == "l":
    #
    #         # Grass underneath the leaves
    #         WIN.blit(Constants.TILES["G"], (self.pos[0] * Constants.SCALE - (self.camera_pos[0] * Constants.SCALE),
    #                                         self.pos[1] * Constants.SCALE - (self.camera_pos[1] * Constants.SCALE)))
    #
    #         # Player
    #         WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (self.camera_pos[0] * Constants.SCALE),
    #                                self.pos[1] * Constants.SCALE - (self.camera_pos[1] * Constants.SCALE)))
    #         # Changing leaf transparency and drawing it
    #         tile.set_alpha(200)
    #         WIN.blit(tile, (self.pos[0] * Constants.SCALE - (self.camera_pos[0] * Constants.SCALE),
    #                         self.pos[1] * Constants.SCALE - (self.camera_pos[1] * Constants.SCALE)))
    #     else:
    #         # Return the leaf to normal transparency
    #         tile.set_alpha(255)
    #         WIN.blit(self.sprite, (self.pos[0] * Constants.SCALE - (self.camera_pos[0] * Constants.SCALE),
    #                                self.pos[1] * Constants.SCALE - (self.camera_pos[1] * Constants.SCALE)))

    def change_equipped(self, old_nitzamon, new_nitzamon):
        if old_nitzamon not in self.nitzamons:
            return
        old_index = self.nitzamon_bag.index(old_nitzamon)
        self.nitzamon_bag.remove(old_nitzamon)
        self.nitzamon_bag.remove(new_nitzamon)
        self.nitzamon_bag.insert(old_index, new_nitzamon)
        self.nitzamon_bag.append(old_nitzamon)

        old_index = self.nitzamons.index(old_nitzamon)
        self.nitzamons.remove(old_nitzamon)
        self.nitzamons.insert(old_index, new_nitzamon)

    def delete_nitzamon(self, nitzamon):
        self.nitzamon_bag.remove(nitzamon)
        if nitzamon in self.nitzamons:
            self.nitzamons.remove(nitzamon)
            if len(self.nitzamon_bag) > 3:
                self.nitzamons.append(self.nitzamon_bag[3])
