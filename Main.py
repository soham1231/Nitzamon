import time
import pygame
import random
import json

import Constants
from Constants import WIN
from Classes.CharacterClasses import Player, Enemy
from Classes.NitzamonClasses import Nitzamon
from Worlds import WorldFunctions
import Fight
from Classes.CharacterClasses import Dialogue


pygame.init()
pygame.display.set_caption("Nitzamon!! ")


def draw_world(world, player):
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

    for y in range(j_min, j_max):
        for x in range(i_min, i_max):
            tile = Constants.TILES[world[y][x]]
            WIN.blit(tile, (x * Constants.SCALE - (player.camera_pos[0] * Constants.SCALE),
                            y * Constants.SCALE - (player.camera_pos[1] * Constants.SCALE)))


def save(player, enemy):

    info = {
        "name": player.name,
        "pos": player.pos,
        "nitzamon_bag": player.nitzamon_bag,
        "active_quests": player.active_quests,
        "world": player.world
    }
    nitzamon_info = {}
    for i in player.nitzamons:
        nitzamon_info[i.name] = json.dumps(i.__dict__)
    print(nitzamon_info)


def main():
    world = WorldFunctions.read_world(Constants.WORLD1_PATH)

    player_nitzamon = Nitzamon.Nitzamon("Shoham", 100, 100, 120, 40, 40, Constants.NPC_IMAGE, Constants.WATER, [])
    player = Player.Player("Shoham", Constants.PLAYER_IMAGE, [1, 1], [player_nitzamon], 0, 0, world)
    player.camera()

    enemy_nitzamon = Nitzamon.Nitzamon("Adi", 50, 50, 60, 30, 30, Constants.NPC_IMAGE, Constants.FIRE, [])

    dialogs = [Dialogue.Dialogue("Hi", 0), Dialogue.Dialogue("H1", 0)]
    enemy = Enemy.Enemy("Adi", Constants.NPC_IMAGE, [5, 5], [enemy_nitzamon], dialogs, world)

    fight_menu = Fight.FightMenu(player.nitzamons, enemy.nitzamons)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(Constants.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if fight_menu.in_fight:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    fight_menu.run(pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        if world[player.pos[1]][player.pos[0]] == "T":
            passed_time = time.time() - fight_menu.fight_start
            if random.randint(1, 100) == 100 and passed_time > Constants.FIGHT_COOL_DOWN:  # 10% chance of fighting and checking if enough time passed since the last fight
                fight_menu.in_fight = True

        if fight_menu.in_fight:
            fight_menu.draw_screen()
            fight_menu.check_hovers(pygame.mouse.get_pos())
            # WIN.blit(pygame.transform.scale(pygame.image.load("Assets\\Menus\\Fight.PNG"), (Constants.X, Constants.Y)), (0, 0))

        else:
            player.camera()
            draw_world(world, player)
            player.move(keys)
            player.draw(player.camera_pos)
            enemy.draw(player.camera_pos)

        pygame.display.update()
    return run


if __name__ == "__main__":
    main()
