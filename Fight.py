import time

import pygame
import Inventory
import Constants
import random


class FightMenu:
    def __init__(self):

        self.player_nitzamons = None
        self.enemy_nitzamons = None

        self.equipped_player_nitzamon = None
        self.equipped_enemy_nitzamon = None

        self.info_text = None

        self.playerTurn = None
        if self.playerTurn:
            self.enemy_attack_time = 0
        else:
            self.enemy_attack_time = time.time()
        self.sound_delay = 0
        self.in_fight = False
        self.changing_nitzamons = False
        self.attacking = False
        self.fight_start = time.time()

        self.background = pygame.transform.scale(pygame.image.load("Assets\\Gemgem bg.png"), (Constants.X, Constants.Y - 250))

        self.main_rect = pygame.Rect((0, Constants.Y - 250), (Constants.X, 250))
        self.topLeft_rect = pygame.Rect((Constants.X - 500, Constants.Y - 200), (170, 50))
        self.topRight_rect = pygame.Rect((Constants.X - 250, Constants.Y - 200), (170, 50))
        self.bottomLeft_rect = pygame.Rect((Constants.X - 500, Constants.Y - 100), (170, 50))
        self.bottomRight_rect = pygame.Rect((Constants.X - 250, Constants.Y - 100), (170, 50))

        self.enemy_nitzamon_info = pygame.Rect((Constants.X - 360, 10), (350, 200))
        self.player_nitzamon_info = pygame.Rect((10, 10), (350, 200))

        self.topLeft_rect_color = Constants.BLACK
        self.topRight_rect_color = Constants.BLACK
        self.bottomLeft_rect_color = Constants.BLACK
        self.bottomRight_rect_color = Constants.BLACK

        self.font = pygame.font.SysFont("arial", Constants.FIGHT_FONT_SIZE)
        self.fight_text = self.font.render("Fight", True, Constants.WHITE)
        self.inventory_text = self.font.render("Inventory", True, Constants.WHITE)
        self.catch_text = self.font.render("Catch", True, Constants.WHITE)
        self.run_text = self.font.render("Run", True, Constants.WHITE)

        self.player_nitzamon_name = None
        self.player_nitzamon_hp = None
        self.player_nitzamon_lvl = None
        self.player_nitzamon_element = None

        self.enemy_nitzamon_name = None
        self.enemy_nitzamon_hp = None
        self.enemy_nitzamon_lvl = None
        self.enemy_nitzamon_element = None

    def draw_screen(self):
        self.change_info()

        Constants.WIN.blit(self.background, (0, 0))
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.main_rect)
        pygame.draw.rect(Constants.WIN, self.topLeft_rect_color, self.topLeft_rect)
        pygame.draw.rect(Constants.WIN, self.topRight_rect_color, self.topRight_rect)
        pygame.draw.rect(Constants.WIN, self.bottomLeft_rect_color, self.bottomLeft_rect)
        pygame.draw.rect(Constants.WIN, self.bottomRight_rect_color, self.bottomRight_rect)
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.enemy_nitzamon_info)
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.player_nitzamon_info)

        Constants.WIN.blit(self.fight_text, (self.topLeft_rect.x + 50, self.topLeft_rect.y + 5))
        Constants.WIN.blit(self.inventory_text, (self.topRight_rect.x + 30, self.topRight_rect.y + 5))
        Constants.WIN.blit(self.catch_text, (self.bottomLeft_rect.x + 50, self.bottomLeft_rect.y + 5))
        Constants.WIN.blit(self.run_text, (self.bottomRight_rect.x + 60, self.bottomRight_rect.y + 5))

        Constants.WIN.blit(self.player_nitzamon_name,
                           (self.player_nitzamon_info.x + 10,
                            self.player_nitzamon_info.y + 10))

        Constants.WIN.blit(self.player_nitzamon_hp,
                           (self.player_nitzamon_info.x + 10,
                            self.player_nitzamon_info.y + 20 + Constants.FIGHT_FONT_SIZE))

        Constants.WIN.blit(self.player_nitzamon_lvl,
                           (self.player_nitzamon_info.x + 10,
                            self.player_nitzamon_info.y + 30 + 2 * Constants.FIGHT_FONT_SIZE))

        Constants.WIN.blit(self.player_nitzamon_element,
                           (self.player_nitzamon_info.x + 10,
                            self.player_nitzamon_info.y + 40 + 3 * Constants.FIGHT_FONT_SIZE))

        Constants.WIN.blit(self.enemy_nitzamon_name,
                           (self.enemy_nitzamon_info.x + 10, self.enemy_nitzamon_info.y + 10))

        Constants.WIN.blit(self.enemy_nitzamon_hp,
                           (self.enemy_nitzamon_info.x + 10,
                            self.enemy_nitzamon_info.y + 20 + Constants.FIGHT_FONT_SIZE))

        Constants.WIN.blit(self.enemy_nitzamon_lvl,
                           (self.enemy_nitzamon_info.x + 10,
                            self.enemy_nitzamon_info.y + 30 + 2 * Constants.FIGHT_FONT_SIZE))

        Constants.WIN.blit(self.enemy_nitzamon_element,
                           (self.enemy_nitzamon_info.x + 10,
                            self.enemy_nitzamon_info.y + 40 + 3 * Constants.FIGHT_FONT_SIZE))

        player_nitzamon_sprite = pygame.transform.scale(self.equipped_player_nitzamon.sprite, (int(Constants.X / 6.4), int(Constants.Y / 3.6)))
        enemy_nitzamon_sprite = pygame.transform.scale(self.equipped_enemy_nitzamon.sprite, (int(Constants.X / 6.4), int(Constants.Y / 3.6)))
        enemy_nitzamon_sprite = pygame.transform.flip(enemy_nitzamon_sprite, True, False)
        Constants.WIN.blit(player_nitzamon_sprite, (100, self.player_nitzamon_info.y + 250))
        Constants.WIN.blit(enemy_nitzamon_sprite, (Constants.X - 300, self.enemy_nitzamon_info.y + 250))

    # Checking if the mouse is hovering over the buttons, if it is, the buttons will change color
    def check_hovers(self, pos):
        if self.topLeft_rect.collidepoint(pos):
            self.topLeft_rect_color = Constants.HOVER_COLOR
        elif self.topRight_rect.collidepoint(pos):
            self.topRight_rect_color = Constants.HOVER_COLOR
        elif self.bottomLeft_rect.collidepoint(pos):
            self.bottomLeft_rect_color = Constants.HOVER_COLOR
        elif self.bottomRight_rect.collidepoint(pos):
            self.bottomRight_rect_color = Constants.HOVER_COLOR
        else:
            self.topLeft_rect_color = Constants.BLACK
            self.topRight_rect_color = Constants.BLACK
            self.bottomLeft_rect_color = Constants.BLACK
            self.bottomRight_rect_color = Constants.BLACK

    def run(self, pos):
        if self.bottomRight_rect.collidepoint(pos):
            if random.randint(1, 10) == 10:
                self.in_fight = False
                self.fight_start = time.time()
            self.playerTurn = False
            self.sound_delay = time.time()

    def draw_attack(self):
        self.draw_screen()
        move1 = self.font.render(self.equipped_player_nitzamon.list_of_moves[0].name, True, Constants.WHITE)
        move2 = self.font.render(self.equipped_player_nitzamon.list_of_moves[1].name, True, Constants.WHITE)
        move3 = self.font.render(self.equipped_player_nitzamon.list_of_moves[2].name, True, Constants.WHITE)
        move4 = self.font.render(self.equipped_player_nitzamon.list_of_moves[3].name, True, Constants.WHITE)
        # if self.equipped_player_nitzamon.list_of_moves[0].element == Constants.FIRE:
        #     pygame.draw.rect(Constants.WIN, (255, 0, 0), self.topLeft_rect)
        pygame.draw.rect(Constants.WIN, self.topLeft_rect_color, self.topLeft_rect)
        pygame.draw.rect(Constants.WIN, self.topRight_rect_color, self.topRight_rect)
        pygame.draw.rect(Constants.WIN, self.bottomLeft_rect_color, self.bottomLeft_rect)
        pygame.draw.rect(Constants.WIN, self.bottomRight_rect_color, self.bottomRight_rect)

        Constants.WIN.blit(move1, (self.topLeft_rect.x + 50, self.topLeft_rect.y + 5))
        Constants.WIN.blit(move2, (self.topRight_rect.x + 30, self.topRight_rect.y + 5))
        Constants.WIN.blit(move3, (self.bottomLeft_rect.x + 50, self.bottomLeft_rect.y + 5))
        Constants.WIN.blit(move4, (self.bottomRight_rect.x + 60, self.bottomRight_rect.y + 5))

        if self.info_text is not None:
            Constants.WIN.blit(self.info_text, (50, Constants.Y - 150))

        self.change_info()

        # pygame.draw.rect(Constants.WIN, Constants.GREY, self.enemy_nitzamon_info)
        # pygame.draw.rect(Constants.WIN, Constants.GREY, self.player_nitzamon_info)
        # Constants.WIN.blit(self.player_nitzamon_name,
        #                    (self.player_nitzamon_info.x + 10,
        #                     self.player_nitzamon_info.y + 10))
        #
        # Constants.WIN.blit(self.player_nitzamon_hp,
        #                    (self.player_nitzamon_info.x + 10,
        #                     self.player_nitzamon_info.y + 20 + Constants.FIGHT_FONT_SIZE))
        # Constants.WIN.blit(self.player_nitzamon_lvl,
        #                    (self.player_nitzamon_info.x + 10,
        #                     self.player_nitzamon_info.y + 30 + 2 * Constants.FIGHT_FONT_SIZE))
        #
        # Constants.WIN.blit(self.player_nitzamon_element,
        #                    (self.player_nitzamon_info.x + 10,
        #                     self.player_nitzamon_info.y + 40 + 3 * Constants.FIGHT_FONT_SIZE))
        #
        # Constants.WIN.blit(self.enemy_nitzamon_name,
        #                    (self.enemy_nitzamon_info.x + 10, self.enemy_nitzamon_info.y + 10))
        #
        # Constants.WIN.blit(self.enemy_nitzamon_hp,
        #                    (self.enemy_nitzamon_info.x + 10,
        #                     self.enemy_nitzamon_info.y + 20 + Constants.FIGHT_FONT_SIZE))
        #
        # Constants.WIN.blit(self.enemy_nitzamon_lvl,
        #                    (self.enemy_nitzamon_info.x + 10,
        #                     self.enemy_nitzamon_info.y + 30 + 2 * Constants.FIGHT_FONT_SIZE))
        #
        # Constants.WIN.blit(self.enemy_nitzamon_element,
        #                    (self.enemy_nitzamon_info.x + 10,
        #                     self.enemy_nitzamon_info.y + 40 + 3 * Constants.FIGHT_FONT_SIZE))

    def attack(self, pos):
        self.check_hovers(pos)
        attack_move = None
        if self.topLeft_rect.collidepoint(pos):
            attack_move = self.equipped_player_nitzamon.list_of_moves[0]

        elif self.topRight_rect.collidepoint(pos):
            attack_move = self.equipped_player_nitzamon.list_of_moves[1]

        elif self.bottomLeft_rect.collidepoint(pos):
            attack_move = self.equipped_player_nitzamon.list_of_moves[2]

        elif self.bottomRight_rect.collidepoint(pos):
            attack_move = self.equipped_player_nitzamon.list_of_moves[3]

        if attack_move is None:
            return

        attack_move.sound.play()

        effectiveness = attack_move.get_effectiveness(self.equipped_enemy_nitzamon)
        self.info_text = self.font.render(f"{self.equipped_player_nitzamon.name} used {attack_move.name}! It was {effectiveness.lower()}!", True, Constants.BLACK)
        damage = int((self.equipped_player_nitzamon.dmg + attack_move.dmg) / 2)
        if effectiveness == "Super effective":
            damage *= 2
        elif effectiveness == "Not very effective":
            damage = int(damage * 0.5)
        self.playerTurn = False
        self.enemy_attack_time = time.time()

        self.equipped_enemy_nitzamon.hp -= damage
        self.change_info()
        self.sound_delay = time.time()

    def change_nitzamons(self, new_nitzamon):
        self.equipped_player_nitzamon = new_nitzamon
        self.playerTurn = False
        self.enemy_attack_time = time.time()
        self.equipped_player_nitzamon.entrance_sound.play()
        self.sound_delay = time.time()

    def start_fight_single(self, player_nitzamons, nitzamon):
        self.player_nitzamons = player_nitzamons
        self.equipped_player_nitzamon = player_nitzamons[0]
        self.change_dead_player_nitzamons()
        self.enemy_nitzamons = nitzamon
        self.equipped_enemy_nitzamon = nitzamon
        self.playerTurn = self.equipped_player_nitzamon.spd >= self.equipped_enemy_nitzamon.spd

        if nitzamon.name == Constants.DARK_SQUARION or nitzamon.name == Constants.GEM_TRIO:
            bg = "Gemgem"
        elif nitzamon.name == Constants.PENTAGEON or nitzamon.name == Constants.TRION:
            bg = "Gemgem"
        elif nitzamon.name == Constants.HEADEA or nitzamon.name == Constants.MANAGEREON or nitzamon.name == Constants.MASMERION:
            bg = "Masmer"
        else:
            bg = "Nitzagram"

        self.background = pygame.transform.scale(pygame.image.load(f"Assets\\{bg} bg.png"), (Constants.X, Constants.Y - 250))
        self.in_fight = True
        self.playerTurn = self.equipped_player_nitzamon.spd >= self.equipped_enemy_nitzamon.spd
        if self.playerTurn:
            self.enemy_attack_time = 0
        else:
            self.enemy_attack_time = time.time()
        self.sound_delay = time.time()
        self.equipped_player_nitzamon.entrance_sound.play()

    def start_fight_enemy(self, player_nitzamons, enemy_nitzamons):
        self.player_nitzamons = player_nitzamons
        self.equipped_player_nitzamon = player_nitzamons[0]
        self.change_dead_player_nitzamons()
        self.enemy_nitzamons = enemy_nitzamons
        self.equipped_enemy_nitzamon = enemy_nitzamons[0]
        self.in_fight = True
        self.playerTurn = self.equipped_player_nitzamon.spd >= self.equipped_enemy_nitzamon.spd
        if self.playerTurn:
            self.enemy_attack_time = 0
        else:
            self.enemy_attack_time = time.time()

        self.sound_delay = time.time()
        self.equipped_player_nitzamon.entrance_sound.play()

    # Changes the onScreen info
    def change_info(self):
        self.player_nitzamon_name = self.font.render(f"Name: {self.equipped_player_nitzamon.name}", True, Constants.BLACK)
        self.player_nitzamon_hp = self.font.render(f"HP: {self.equipped_player_nitzamon.hp}/{self.equipped_player_nitzamon.max_hp}", True, Constants.BLACK)
        self.player_nitzamon_lvl = self.font.render(f"Level: {self.equipped_player_nitzamon.lvl}", True, Constants.BLACK)
        self.player_nitzamon_element = self.font.render(f"Element: {self.equipped_player_nitzamon.element}", True, Constants.BLACK)

        self.enemy_nitzamon_name = self.font.render(f"Name: {self.equipped_enemy_nitzamon.name}", True, Constants.BLACK)
        self.enemy_nitzamon_hp = self.font.render(f"HP: {self.equipped_enemy_nitzamon.hp}/{self.equipped_enemy_nitzamon.max_hp}", True, Constants.BLACK)
        self.enemy_nitzamon_lvl = self.font.render(f"Level: {self.equipped_enemy_nitzamon.lvl}", True, Constants.BLACK)
        self.enemy_nitzamon_element = self.font.render(f"Element: {self.equipped_enemy_nitzamon.element}", True, Constants.BLACK)

    # Enemy attacking
    def enemy_attack(self):
        move1 = self.equipped_enemy_nitzamon.list_of_moves[0]
        move2 = self.equipped_enemy_nitzamon.list_of_moves[1]
        move3 = self.equipped_enemy_nitzamon.list_of_moves[2]
        move4 = self.equipped_enemy_nitzamon.list_of_moves[3]
        moves = [move1, move2, move3, move4]

        chosen_move = random.choice(moves)
        chosen_move.sound.play()
        self.sound_delay = time.time()

        effectiveness = chosen_move.get_effectiveness(self.equipped_enemy_nitzamon.element)
        self.info_text = self.font.render(f"{self.equipped_enemy_nitzamon.name} used {chosen_move.name}! It was {effectiveness.lower()}!", True, Constants.BLACK)
        # Calculating damage
        damage = int((self.equipped_player_nitzamon.dmg + chosen_move.dmg) / 2)
        if chosen_move.get_effectiveness(self.equipped_enemy_nitzamon.element) == "Super effective":
            damage *= 2
        elif chosen_move.get_effectiveness(self.equipped_enemy_nitzamon.element) == "Not very effective":
            damage = int(damage * 0.5)

        self.equipped_player_nitzamon.hp -= damage
        self.change_info()
        self.playerTurn = True

    # If the nitzamon is dead, switch to another
    def change_dead_player_nitzamons(self):
        if self.equipped_player_nitzamon.hp <= 0:
            self.equipped_player_nitzamon.hp = 0
            self.equipped_player_nitzamon.death_sound.play()
            for nitzamon in self.player_nitzamons:
                if nitzamon.hp > 0:
                    self.equipped_player_nitzamon = nitzamon
                    self.equipped_player_nitzamon.entrance_sound.play()
                    self.sound_delay = time.time()
                    break

    def handle_events(self):
        if self.playerTurn and not self.attacking and time.time() - self.sound_delay >= 2:
            self.run(pygame.mouse.get_pos())

        if self.topRight_rect.collidepoint(pygame.mouse.get_pos()) and not self.attacking:
            self.changing_nitzamons = True

        if time.time() - self.sound_delay >= 2:
            if self.changing_nitzamons:
                replacing = Inventory.check_collision(pygame.mouse.get_pos(), self.player_nitzamons)
                if replacing is not None:
                    self.change_nitzamons(replacing)
                    self.changing_nitzamons = False
            if self.attacking and self.playerTurn:
                self.attack(pygame.mouse.get_pos())
        if self.topLeft_rect.collidepoint(pygame.mouse.get_pos()) and not self.changing_nitzamons:
            self.attacking = True

    def level_up_nitzamons(self):
        lvl_sum = 0
        if type(self.enemy_nitzamons) == list:
            for nitzamon in self.enemy_nitzamons:
                if nitzamon.lvl > self.equipped_player_nitzamon.lvl:
                    lvl_sum += 5
                else:
                    lvl_sum += 3
        else:
            if self.equipped_enemy_nitzamon.lvl > self.equipped_player_nitzamon.lvl:
                lvl_sum += 5
            else:
                lvl_sum += 4
        self.equipped_player_nitzamon.level_up(lvl_sum)
        for nitzamon in self.player_nitzamons:
            if nitzamon != self.equipped_player_nitzamon:
                nitzamon.level_up(int(lvl_sum / 3))

    def evolve_animation(self):
        pass

    def handle_fight_encounter(self):
        if self.player_won():
            self.level_up_nitzamons()
            self.end_fight()
        elif self.enemy_won():  # Two different if statements because we may want to add rewards when player wins
            self.end_fight()
        if time.time() - self.sound_delay >= 2:
            self.change_deaths()
        if not self.playerTurn:
            if time.time() - self.enemy_attack_time >= 2:
                self.enemy_attack()
        if self.changing_nitzamons:
            Inventory.draw_inventory(self.player_nitzamons)
        elif self.attacking:
            self.draw_attack()
        else:
            self.draw_screen()
        self.check_hovers(pygame.mouse.get_pos())

    # If any of the nitzamons die(player or enemy) switch to a different one
    def change_deaths(self):
        self.change_dead_player_nitzamons()

        if self.equipped_enemy_nitzamon.hp <= 0:
            self.equipped_enemy_nitzamon.hp = 0
            self.equipped_enemy_nitzamon.death_sound.play()
            if type(self.enemy_nitzamons) == list:
                for nitzamon in self.enemy_nitzamons:
                    if nitzamon.hp > 0:
                        self.equipped_enemy_nitzamon = nitzamon
                        self.equipped_enemy_nitzamon.entrance_sound.play()
                        self.sound_delay = time.time()
                        break
            else:
                self.end_fight()

        self.change_info()
        if self.attacking:
            self.draw_screen()

    def end_fight(self):
        self.in_fight = False
        self.attacking = False
        self.changing_nitzamons = False
        self.fight_start = time.time()

    def player_won(self):
        if self.equipped_enemy_nitzamon.hp <= 0:
            if type(self.enemy_nitzamons) == list:
                for nitzamon in self.enemy_nitzamons:
                    if nitzamon.hp > 0:
                        return False
                self.equipped_enemy_nitzamon.hp = 0
                return True
            else:
                self.equipped_enemy_nitzamon.hp = 0
                return True
        return False

    def enemy_won(self):
        if self.equipped_player_nitzamon.hp <= 0:
            for nitzamon in self.player_nitzamons:
                if nitzamon.hp > 0:
                    return False
            self.equipped_player_nitzamon.hp = 0
            return True
        return False

    def catch(self, player):
        self.playerTurn = False
        player.nitzaballs -= 1
        catched = False
        nitzamon_hp = (self.equipped_enemy_nitzamon.hp / self.equipped_enemy_nitzamon.max_hp) * 100
        if nitzamon_hp < 25:
            if random.randint(1, 4) == 1:
                catched = True
        elif nitzamon_hp < 50:
            if random.randint(1, 8) == 1:
                catched = True
        elif nitzamon_hp < 75:
            if random.randint(1, 12) == 1:
                catched = True
        else:
            if random.randint(1, 16) == 1:
                catched = True

        if catched:
            self.equipped_enemy_nitzamon.hp = self.equipped_enemy_nitzamon.max_hp
            player.nitzamon_bag.append(self.equipped_enemy_nitzamon)
            self.end_fight()