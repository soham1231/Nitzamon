import time
import pygame
import random
import json

import Constants
from Constants import WIN
from Classes.NitzamonClasses import Nitzamon
from Worlds import WorldFunctions
import Fight
from Classes.CharacterClasses import Enemy, Player, NPC
import EnemyNitzamons
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


def draw_npcs(npcs, camera_pos):  # NUMBER OF N'S ON THE MAP MUST BE EQUAL TO NUMBER OF NPCS!
    for npc in npcs:
        npc.draw(camera_pos)


def random_nitzamon():
    name = random.choice(Constants.NAMES)
    level = random.randint(1, 100)
    health = level + random.randint(level * 2, level * 4)
    element = Constants.NITZAMON_ELEMENTS_DICT[name]
    fire_moves = Constants.FIRE_MOVES
    water_moves = Constants.WATER_MOVES
    earth_moves = Constants.EARTH_MOVES
    normal_moves = Constants.NORMAL_MOVES

    if element == Constants.FIRE:
        move1 = random.choice(fire_moves)
        tmp_move = fire_moves.pop(fire_moves.index(move1))
        move2 = random.choice(fire_moves)
        fire_moves.append(tmp_move)
    elif element == Constants.EARTH:
        move1 = random.choice(earth_moves)
        tmp_move = earth_moves.pop(earth_moves.index(move1))
        move2 = random.choice(earth_moves)
        earth_moves.append(tmp_move)
    else:
        move1 = random.choice(water_moves)
        tmp_move = water_moves.pop(water_moves.index(move1))
        move2 = random.choice(water_moves)
        water_moves.append(tmp_move)

    move3 = random.choice(normal_moves)
    tmp_move = normal_moves.pop(normal_moves.index(move3))
    move4 = random.choice(normal_moves)
    normal_moves.append(tmp_move)
    entrance_sound = pygame.mixer.Sound(f"Assets\\Sounds\\Fight Entrance\\{name}.mp3")
    death_sound = pygame.mixer.Sound(f"Assets\\Sounds\\Death\\{name}.mp3")

    return Nitzamon.Nitzamon(name, level, [move1, move2, move3, move4])


def save(player, enemy):  # Probably gonna remove it
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


def npcs_in_range(npcs, pos):  # Im thinking of moving it to Player class
    for npc in npcs:
        if ((pos[0] == npc.pos[0] - 1) and (pos[1] == npc.pos[1])) or \
                ((pos[0] == npc.pos[0]) and (pos[1] == npc.pos[1] + 1)) or \
                ((pos[0] == npc.pos[0] + 1) and (pos[1] == npc.pos[1])) or \
                ((pos[0] == npc.pos[0]) and (pos[1] == npc.pos[1] - 1)):
            return True, npc
    return False, None


def draw_starters():  # Leave this to Adi
    WIN.fill(Constants.GREY)
    font = pygame.font.SysFont("Comic Sans MS", int((Constants.X + Constants.Y) / 16))
    text = font.render("Choose your starter", True, Constants.WHITE)
    WIN.blit(text, (Constants.X / 2 - text.get_width() / 2, int(Constants.Y / 36) - 25))
    font = pygame.font.SysFont("Comic Sans MS", int((Constants.X + Constants.Y) / 125))

    nitzaphone_sprite = pygame.transform.scale(Constants.NITZAPHONE_STARTER.sprite, (200, 200))
    nitzaphone_name = font.render("Name: " + Constants.NITZAPHONE, True, Constants.WHITE)
    nitzaphone_element = font.render("Element: " + Constants.NITZAMON_ELEMENTS_DICT[Constants.NITZAPHONE], True, Constants.WHITE)
    WIN.blit(nitzaphone_name, (Constants.X / 3.5 - nitzaphone_sprite.get_width(), Constants.Y / 2))
    WIN.blit(nitzaphone_element, (Constants.X / 3.5 - nitzaphone_sprite.get_width(), Constants.Y / 2 + font.get_height()))
    WIN.blit(nitzaphone_sprite, (Constants.X / 3.5 - nitzaphone_sprite.get_width(), Constants.Y / 2 - nitzaphone_sprite.get_height()))

    gem_trio_sprite = pygame.transform.scale(Constants.GEM_TRIO_STARTER.sprite, (200, 200))
    gem_trio_name = font.render("Name: " + Constants.GEM_TRIO, True, Constants.WHITE)
    gem_trio_element = font.render("Element: " + Constants.NITZAMON_ELEMENTS_DICT[Constants.GEM_TRIO], True, Constants.WHITE)
    WIN.blit(gem_trio_name, (Constants.X * (2/3.5) - gem_trio_sprite.get_width(), Constants.Y / 2))
    WIN.blit(gem_trio_element, (Constants.X * (2/3.5) - gem_trio_sprite.get_width(), Constants.Y / 2 + font.get_height()))
    WIN.blit(gem_trio_sprite, (Constants.X * (2/3.5) - gem_trio_sprite.get_width(), Constants.Y / 2 - gem_trio_sprite.get_height()))

    masmerion_sprite = pygame.transform.scale(Constants.MASMERION_STARTER.sprite, (200, 200))
    masmerion_name = font.render("Name: " + Constants.MASMERION, True, Constants.WHITE)
    masmerion_element = font.render("Element: " + Constants.NITZAMON_ELEMENTS_DICT[Constants.MASMERION], True, Constants.WHITE)
    WIN.blit(masmerion_name, (Constants.X * (3/3.5) - masmerion_sprite.get_width(), Constants.Y / 2))
    WIN.blit(masmerion_element, (Constants.X * (3/3.5) - masmerion_sprite.get_width(), Constants.Y / 2 + font.get_height()))
    WIN.blit(masmerion_sprite, (Constants.X * (3/3.5) - masmerion_sprite.get_width(), Constants.Y / 2 - masmerion_sprite.get_height()))


def choose_starters(player, pos):
    nitzamon = None
    if Constants.Y / 2 - 200 <= pos[1] <= Constants.Y / 2:
        if Constants.X / 3.5 - 200 <= pos[0] <= Constants.X / 3.5:
            nitzamon = Constants.NITZAPHONE_STARTER
        elif Constants.X * (2/3.5) - 200 <= pos[0] <= Constants.X * (2/3.5):
            nitzamon = Constants.GEM_TRIO_STARTER
        elif Constants.X * (3/3.5) - 200 <= pos[0] <= Constants.X * (3/3.5):
            nitzamon = Constants.MASMERION_STARTER

    if nitzamon is not None:
        player.nitzamons.append(nitzamon)
        player.nitzamon_bag.append(nitzamon)
        return True
    return False


def main():
    world = WorldFunctions.read_world(Constants.WORLD1_PATH)

    # npcs
    # guide: create a new npc and add it to npc_list
    roni = NPC.NPC("Roni", Constants.NPC_SPRITE_RONI, Constants.NPC_PFP_RONI, (5, 5), [], ["HI! HELLO!"], world)
    npc_list = [roni]
    talked_to = False
    npc = None

    # Enemies
    shoham_nitzamons = [EnemyNitzamons.shoham_nitzamon1, EnemyNitzamons.shoham_nitzamon2, EnemyNitzamons.shoham_nitzamon3]
    shoham = Enemy.Enemy("Shoham", Constants.SHOHAM_NPC, (3, 29), shoham_nitzamons, world, True)

    gilad_nitzamons = [EnemyNitzamons.gilad_nitzamon1, EnemyNitzamons.gilad_nitzamon2, EnemyNitzamons.gilad_nitzamon3]
    gilad = Enemy.Enemy("Gilad", Constants.GILAD_NPC, (17, 84), gilad_nitzamons, world, True)

    adi_nitzamons = [EnemyNitzamons.adi_nitzamon1, EnemyNitzamons.adi_nitzamon2, EnemyNitzamons.adi_nitzamon3]
    adi = Enemy.Enemy("Adi", Constants.ADI_NPC, (92, 49), adi_nitzamons, world, True)

    enemy_list = [shoham, gilad, adi]

    # nitzamon_list = []
    # equipped = []
    # for i in range(20):  # Leave this until we add the ability to catch nitzamons
    #     nitzamon_list.append(random_nitzamon())
    # for i in range(3):
    #     equipped.append(random_nitzamon())
    player = Player.Player("Shoham", Constants.PLAYER_IMAGE, [1, 1], [], [], 0, world, {"Gem": 1})
    nitzamon_pressed = None

    fight_menu = Fight.FightMenu()
    clock = pygame.time.Clock()

    choosing_starter = True
    run = True
    while run:
        clock.tick(Constants.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                fight_menu.handle_events()

                if choosing_starter:
                    if choose_starters(player, pygame.mouse.get_pos()):
                        choosing_starter = False

                # Checking if the player pressed a nitzamon in inventory
                if Inventory.is_open and not (Inventory.info_open or Inventory.equip_open):
                    nitzamon_pressed = Inventory.check_collision(pygame.mouse.get_pos(), player.nitzamon_bag)
                    if nitzamon_pressed is not None:
                        Inventory.info_open = True
                # Checking if the player is pressing the "equip"
                if Inventory.info_open and Inventory.equip_rect.collidepoint(pygame.mouse.get_pos()):
                    Inventory.equip_open = True
                # Checking if the player is pressing the "remove" button
                elif Inventory.info_open and Inventory.remove_rect.collidepoint(pygame.mouse.get_pos()):
                    player.delete_nitzamon(nitzamon_pressed)
                    Inventory.info_open = False
                # If the player pressed the "equip" button, it will open the inventory again and check if the player
                # Has pressed another nitzamon
                if Inventory.equip_open:
                    new_nitzamon = Inventory.check_collision(pygame.mouse.get_pos(), player.nitzamon_bag)
                    if new_nitzamon is not None:
                        player.change_equipped(nitzamon_pressed, new_nitzamon)
                        Inventory.equip_open = False
                        Inventory.info_open = False

            if event.type == pygame.KEYDOWN:
                # If the player pressed 'e' it will either open or close the inventory
                if event.key == pygame.K_e:
                    Inventory.is_open = not Inventory.is_open
                # Going back to the menu before or quits the game
                if event.key == pygame.K_ESCAPE:
                    if fight_menu.in_fight and fight_menu.changing_nitzamons:
                        fight_menu.changing_nitzamons = False
                    elif fight_menu.in_fight and fight_menu.attacking:
                        fight_menu.attacking = False
                    elif Inventory.equip_open:
                        Inventory.equip_open = False
                    elif Inventory.info_open:
                        Inventory.info_open = False
                    elif Inventory.is_open:
                        Inventory.is_open = False
                    else:
                        run = False
                # If the player pressed the 'f' key it will check if npcs are nearby
                if event.key == pygame.K_f:
                    talked_to, npc = npcs_in_range(npc_list, player.pos)

                if event.key == pygame.K_h:
                    player.heal_nitzamons()
        # Checking if the player is walking on tall grass and not in fight
        if world[player.pos[1]][player.pos[0]] == "T" and not fight_menu.in_fight:
            passed_time = time.time() - fight_menu.fight_start
            # Checking if fight cooldown is over
            if random.randint(1, 100) > 90 and passed_time > Constants.FIGHT_COOL_DOWN:  # 10% chance of fighting and checking if enough time passed since the last fight
                fight_menu.start_fight_single(player.nitzamons, random_nitzamon())

        keys = pygame.key.get_pressed()

        if choosing_starter:
            draw_starters()
        # If the player is in fight, check which screen to draw
        elif fight_menu.in_fight:
            fight_menu.handle_fight_encounter()
        # If the player pressed the 'm' key, draw minimap
        elif keys[pygame.K_m]:
            draw_minimap(world, player)

        # If the inventory is open, check which screen to draw
        elif Inventory.is_open:
            Inventory.draw_inventory(player.nitzamon_bag)
            if Inventory.equip_open:
                Inventory.draw_inventory(player.nitzamon_bag)
            elif Inventory.info_open:
                Inventory.show_info(nitzamon_pressed)
        # Draw the world
        else:
            player.camera()
            draw_world(world, player)
            player.move(keys)
            player.draw(player.camera_pos)
            draw_npcs(npc_list, player.camera_pos)
            draw_npcs(enemy_list, player.camera_pos)
            if talked_to and npc is not None:
                npc.talk(player)
                if not pygame.mixer.get_busy():
                    npc.voice.play()
                if keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s]:
                    talked_to = False
                    npc.voice.stop()
        # pygame.draw.rect(WIN, BLACK, pygame.Rect((0, (3 * Y / 4)), (X, (3 * Y / 4))))
        pygame.display.update()
    return run


if __name__ == "__main__":
    main()
