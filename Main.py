import time
import pygame
import random
import json

import Constants
from Constants import WIN
from Classes.NitzamonClasses import Nitzamon
from Classes.NitzamonClasses import Move
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
    x_center = Constants.X / 2 - Constants.MINI_SCALE / 2 * len(world)
    y_center = Constants.Y / 2 - Constants.MINI_SCALE / 2 * len(world)
    for y in range(len(world)):
        for x in range(len(world)):
            tile = pygame.transform.scale(Constants.TILES[world[y][x]], (Constants.MINI_SCALE, Constants.MINI_SCALE))
            WIN.blit(tile, (x_center + x * Constants.MINI_SCALE, y_center + y * Constants.MINI_SCALE))
    player_image = pygame.transform.scale(player.sprite, (Constants.MINI_SCALE, Constants.MINI_SCALE))
    WIN.blit(player_image,
             (x_center + player.pos[0] * Constants.MINI_SCALE, y_center + player.pos[1] * Constants.MINI_SCALE))


# npcs
# guide: create a new npc, and add it to npc_list
world1 = WorldFunctions.read_world(Constants.WORLD1_PATH)
NPC_SPRITE_RONI = pygame.transform.scale(pygame.image.load("Assets\\Characters\\NPCS\\Roni.jpg"),
                                         (Constants.SCALE, Constants.SCALE))
roni = NPC.NPC("Roni", NPC_SPRITE_RONI, (5, 5), [], [Dialogue.Dialogue("HI! \n HELLO!", None)], world1)
npc_list = [roni]


def draw_npcs(npc_list, camera_pos):  # NUMBER OF N'S ON THE MAP MUST BE EQUAL TO NUMBER OF NPCS!
    for npc in npc_list:
        npc.draw(camera_pos)


def random_move():
    element = random.choice(["fire", "water", "earth"])
    dmg = random.choice([1, 2, 3, 4])
    name = random.choice(["hug", "kiss", "pet", "touch"])
    return Move.Move(element, dmg, name)


def random_nitzamon():
    name = random.choice(Constants.NAMES)
    sprite = pygame.image.load(f"Assets\\Nitzamons\\{name}.png")
    level = random.randint(1, 100)
    health = level + random.randint(50, 400)
    attack = level + random.randint(0, 50)
    speed = level + random.randint(0, 20)
    element = Constants.NITZAMON_ELEMENTS_DICT[name]
    fire_moves = Constants.FIRE_MOVES
    water_moves = Constants.WATER_MOVES
    earth_moves = Constants.EARTH_MOVES
    normal_moves = Constants.NORMAL_MOVES

    if element == Constants.FIRE:
        move1 = random.choice(fire_moves)
        fire_moves.remove(move1)
        move2 = random.choice(fire_moves)
    elif element == Constants.EARTH:
        move1 = random.choice(earth_moves)
        earth_moves.remove(move1)
        move2 = random.choice(earth_moves)
    else:
        move1 = random.choice(water_moves)
        water_moves.remove(move1)
        move2 = random.choice(water_moves)
    move3 = random.choice(normal_moves)
    normal_moves.remove(move3)
    move4 = random.choice(normal_moves)

    return Nitzamon.Nitzamon(name, level, health, health, attack, speed, sprite, element,
                             [move1, move2, move3, move4])


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
    talked_to = False
    npc = None
    nitzamon_list = []
    equipped = []
    for i in range(20):
        nitzamon_list.append(random_nitzamon())
    for i in range(3):
        equipped.append(random_nitzamon())
    equipped[0].spd = 10000
    player = Player.Player("Shoham", Constants.PLAYER_IMAGE, [1, 1], equipped, nitzamon_list, 0, world)
    nitzamon_pressed = None
    player.camera()

    enemy_nitzamon = Nitzamon.Nitzamon("Adi", 50, 50, 60, 30, 30, Constants.NPC_IMAGE, Constants.FIRE, [])

    dialogs = [Dialogue.Dialogue("Hi", 0), Dialogue.Dialogue("H1", 0)]
    enemy = Enemy.Enemy("Adi", Constants.NPC_IMAGE, [5, 5], [enemy_nitzamon], dialogs, world, False)

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
                    if fight_menu.playerTurn and not fight_menu.attacking:
                        fight_menu.run(pygame.mouse.get_pos())

                    if fight_menu.topRight_rect.collidepoint(pygame.mouse.get_pos()) and not fight_menu.attacking:
                        fight_menu.changing_nitzamons = True

                    if fight_menu.changing_nitzamons:
                        replacing = Inventory.check_collision(pygame.mouse.get_pos(), fight_menu.player_nitzamons)
                        if replacing is not None:
                            fight_menu.change_nitzamons(replacing)
                            fight_menu.changing_nitzamons = False
                    if fight_menu.attacking and fight_menu.playerTurn:
                        fight_menu.attack(pygame.mouse.get_pos())
                    if fight_menu.topLeft_rect.collidepoint(pygame.mouse.get_pos()) and not fight_menu.changing_nitzamons:
                        fight_menu.attacking = True

                if Inventory.is_open and not (Inventory.info_open or Inventory.equip_open):
                    nitzamon_pressed = Inventory.check_collision(pygame.mouse.get_pos(), player.nitzamon_bag)
                    if nitzamon_pressed is not None:
                        Inventory.info_open = True
                if Inventory.info_open and Inventory.equip_rect.collidepoint(pygame.mouse.get_pos()):
                    Inventory.equip_open = True
                elif Inventory.info_open and Inventory.remove_rect.collidepoint(pygame.mouse.get_pos()):
                    player.delete_nitzamon(nitzamon_pressed)
                    Inventory.info_open = False
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
                    if fight_menu.in_fight and fight_menu.changing_nitzamons:
                        fight_menu.changing_nitzamons = False
                    elif Inventory.equip_open:
                        Inventory.equip_open = False
                    elif Inventory.info_open:
                        Inventory.info_open = False
                    elif Inventory.is_open:
                        Inventory.is_open = False
                    else:
                        run = False
                if event.key == pygame.K_f:
                    for npc in npc_list:
                        if ((player.pos[0] == npc.pos[0] - 1) and (player.pos[1] == npc.pos[1])) or \
                                ((player.pos[0] == npc.pos[0]) and (player.pos[1] == npc.pos[1] + 1)) or \
                                ((player.pos[0] == npc.pos[0] + 1) and (player.pos[1] == npc.pos[1])) or \
                                ((player.pos[0] == npc.pos[0]) and (player.pos[1] == npc.pos[1] - 1)):
                            print(npc.name)
                            talked_to = True
                            break

        if world[player.pos[1]][player.pos[0]] == "T" and not fight_menu.in_fight:
            passed_time = time.time() - fight_menu.fight_start
            if random.randint(1,
                              100) >= 90 and passed_time > Constants.FIGHT_COOL_DOWN:  # 1% chance of fighting and checking if enough time passed since the last fight
                fight_menu.start_fight_single(player.nitzamons, random_nitzamon())

        keys = pygame.key.get_pressed()
        if fight_menu.in_fight:
            if not fight_menu.playerTurn:
                if time.time() - fight_menu.enemy_attack_time >= 1:
                    fight_menu.enemy_attack()
            if fight_menu.changing_nitzamons:
                Inventory.draw_inventory(player.nitzamons)
            elif fight_menu.attacking:
                fight_menu.draw_attack()
            else:
                fight_menu.draw_screen()
            fight_menu.check_hovers(pygame.mouse.get_pos())

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
            player.move(keys)
            player.draw(player.camera_pos)
            draw_npcs(npc_list, player.camera_pos)
            if talked_to and npc is not None:
                npc.talk(player)
                if keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s]:
                    talked_to = False
        # pygame.draw.rect(WIN, BLACK, pygame.Rect((0, (3 * Y / 4)), (X, (3 * Y / 4))))
        pygame.display.update()
    return run


if __name__ == "__main__":
    main()
