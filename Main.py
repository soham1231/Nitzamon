import pygame
import math

import Constants
from Constants import WIN
from Classes.CharacterClasses import Player
from Worlds import WorldFunctions
import Fight

pygame.init()
pygame.display.set_caption("Nitzamon!! ")
world = WorldFunctions.read_world(Constants.WORLD1_PATH)

player = Player.Player("Shoham", Constants.PLAYER_IMAGE, [0, 0], 0, 0, 0)
player.camera()


def draw_world():
    i_max = len(world)
    j_max = len(world)
    if player.pos[0] + Constants.TILE_ROW < len(world):
        i_max = player.pos[0] + Constants.TILE_ROW
    if player.pos[1] + Constants.TILE_COL < len(world):
        j_max = player.pos[1] + Constants.TILE_COL

    i_min = 0
    j_min = 0
    if player.pos[0] > Constants.TILE_ROW:
        i_min = player.pos[0] - Constants.TILE_ROW
    if player.pos[1] > Constants.TILE_COL:
        j_min = player.pos[1] - Constants.TILE_COL

    for i in range(i_min, i_max):
        for j in range(j_min, j_max):
            tile = Constants.TILES[world[i][j]]
            WIN.blit(tile, (i * Constants.SCALE - (player.camera_pos[0] * Constants.SCALE), j * Constants.SCALE - (player.camera_pos[1] * Constants.SCALE)))


fight_menu = Fight.FightMenu()
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(Constants.fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if world[player.pos[0]][player.pos[1]] != "T":
        player.camera()
        draw_world()
        player.move(keys)
        player.draw_player()
    else:
        fight_menu.draw_screen()
        fight_menu.check_hovers(pygame.mouse.get_pos())

    pygame.display.update()
pygame.quit()
