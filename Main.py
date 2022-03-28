import time
import pygame
import random
import json

import Constants
from Constants import WIN
from Classes.NitzamonClasses import Nitzamon
from Worlds import WorldFunctions
import Fight
from Classes.CharacterClasses import Dialogue, Enemy, Player, NPC
import Inventory


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


def draw_minimap(world, player):
    WIN.fill(Constants.BLACK)
    x_center = Constants.X/2 - Constants.MINI_SCALE/2 * len(world)
    y_center = Constants.Y/2 - Constants.MINI_SCALE/2 * len(world)
    for y in range(len(world)):
        for x in range(len(world)):
            tile = pygame.transform.scale(Constants.TILES[world[y][x]], (Constants.MINI_SCALE, Constants.MINI_SCALE))
            WIN.blit(tile, (x_center + x * Constants.MINI_SCALE, y_center + y * Constants.MINI_SCALE))
    player_image = pygame.transform.scale(player.sprite, (Constants.MINI_SCALE, Constants.MINI_SCALE))
    WIN.blit(player_image, (x_center + player.pos[0] * Constants.MINI_SCALE, y_center + player.pos[1] * Constants.MINI_SCALE))


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
        nitzamon_info = json.dumps(i.__dict__)
    print(nitzamon_info)


def main():
    world = WorldFunctions.read_world(Constants.WORLD1_PATH)
    npc_list = []

    nitzamon_list = []
    for i in range(19):
        if i % 2 == 0:
            nitzamon_list.append(Nitzamon.Nitzamon("Gilad", 90, 100, 100, 40, 0, Constants.PLAYER_IMAGE, Constants.EARTH, []))
        else:
            nitzamon_list.append(Nitzamon.Nitzamon("Shoham", 100, 100, 120, 40, 40, Constants.NPC_IMAGE, Constants.WATER, []))
    equipped1 = Nitzamon.Nitzamon("Adi", 10, 10, 20, 30, 23, Constants.NPC_IMAGE, Constants.WATER, [])
    equipped2 = Nitzamon.Nitzamon("Ori", 116, 143, 201, 332, 50, Constants.NPC_IMAGE, Constants.EARTH, [])
    player = Player.Player("Shoham", Constants.PLAYER_IMAGE, [1, 1], [equipped1, equipped2], nitzamon_list, 0, world)
    nitzamon_pressed = None
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fight_menu.in_fight:
                    fight_menu.run(pygame.mouse.get_pos())
                if Inventory.is_open and not (Inventory.info_open or Inventory.equip_open):
                    nitzamon_pressed = Inventory.check_collision(pygame.mouse.get_pos(), player.nitzamon_bag)
                    if nitzamon_pressed is not None:
                        Inventory.info_open = True
                if Inventory.info_open and Inventory.equip_rect.collidepoint(pygame.mouse.get_pos()):
                    Inventory.equip_open = True
                if Inventory.equip_open:
                    new_nitzamon = Inventory.check_collision(pygame.mouse.get_pos(), player.nitzamon_bag)
                    if new_nitzamon is not None:
                        player.change_equipped(nitzamon_pressed, new_nitzamon)
                        Inventory.equip_open = False
                        Inventory.info_open = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Inventory.is_open = not Inventory.is_open
                if event.key == pygame.K_ESCAPE:
                    if Inventory.equip_open:
                        Inventory.equip_open = False
                    elif Inventory.info_open:
                        Inventory.info_open = False
                    elif Inventory.is_open:
                        Inventory.is_open = False
                    else:
                        run = False

        if world[player.pos[1]][player.pos[0]] == "T":
            passed_time = time.time() - fight_menu.fight_start
            if random.randint(1, 100) == 100 and passed_time > Constants.FIGHT_COOL_DOWN:  # 1% chance of fighting and checking if enough time passed since the last fight
                fight_menu.in_fight = True

        keys = pygame.key.get_pressed()
        if fight_menu.in_fight:
            fight_menu.draw_screen()
            fight_menu.check_hovers(pygame.mouse.get_pos())
            # WIN.blit(pygame.transform.scale(pygame.image.load("Assets\\Menus\\Fight.PNG"), (Constants.X, Constants.Y)), (0, 0))

        elif keys[pygame.K_m]:
            draw_minimap(world, player)
        elif Inventory.is_open:
            Inventory.draw_inventory(player.nitzamon_bag)
            if Inventory.equip_open:
                Inventory.draw_inventory(player.nitzamon_bag)
            elif Inventory.info_open:
                Inventory.show_info(nitzamon_pressed)
        else:
            player.camera()
            draw_world(world, player)
            player.move(pygame.key.get_pressed())
            player.draw()
        # pygame.draw.rect(WIN, BLACK, pygame.Rect((0, (3 * Y / 4)), (X, (3 * Y / 4))))
        pygame.display.update()
    return run


if __name__ == "__main__":
    main()
