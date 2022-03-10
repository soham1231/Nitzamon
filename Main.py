import pygame
import math

import Constants
from Constants import WIN
import Player
import WorldFunctions

pygame.init()
pygame.display.set_caption("Nitzamon!! ")
world = WorldFunctions.read_world("World1")

player_sprite = pygame.image.load("Assets\\Characters\\amongus.png")
player_sprite = pygame.transform.scale(player_sprite, (Constants.SCALE, Constants.SCALE))
player = Player.Player("Shoham", player_sprite, [0, 0])
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
            tile = pygame.transform.scale(Constants.TILES[world[i][j]], (Constants.SCALE, Constants.SCALE))
            WIN.blit(tile, (i * Constants.SCALE - (player.camera_pos[0] * Constants.SCALE), j * Constants.SCALE - (player.camera_pos[1] * Constants.SCALE)))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    player.camera()
    draw_world()
    player.move(keys)
    player.draw_player()

    pygame.display.update()
pygame.quit()
