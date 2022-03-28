import time

import pygame
import Constants
import random
import Inventory


class FightMenu:
    def __init__(self, player_nitzamons, enemy_nitzamons):

        self.player_nitzamons = player_nitzamons
        self.enemy_nitzamons = enemy_nitzamons

        self.equipped_player_nitzamon = self.player_nitzamons[0]
        self.equipped_enemy_nitzamon = self.enemy_nitzamons[0]

        self.in_fight = False
        self.changing_nitzamons = False
        self.fight_start = time.time()

        self.main_rect = pygame.Rect((0, Constants.Y - 250), (Constants.X, 250))
        self.topLeft_rect = pygame.Rect((Constants.X - 500, Constants.Y - 200), (170, 50))
        self.topRight_rect = pygame.Rect((Constants.X - 250, Constants.Y - 200), (170, 50))
        self.bottomLeft_rect = pygame.Rect((Constants.X - 500, Constants.Y - 100), (170, 50))
        self.bottomRight_rect = pygame.Rect((Constants.X - 250, Constants.Y - 100), (170, 50))

        self.enemy_nitzamon_info = pygame.Rect((Constants.X - 360, 10), (350, 200))
        self.player_nitzamon_info = pygame.Rect((10, 10), (350, 200))

        self.fight_rect_color = Constants.BLACK
        self.inventory_rect_color = Constants.BLACK
        self.catch_rect_color = Constants.BLACK
        self.run_rect_color = Constants.BLACK

        self.font = pygame.font.SysFont("arial", Constants.FIGHT_FONT_SIZE)
        self.fight_text = self.font.render("Fight", True, Constants.WHITE)
        self.inventory_text = self.font.render("Inventory", True, Constants.WHITE)
        self.catch_text = self.font.render("Catch", True, Constants.WHITE)
        self.run_text = self.font.render("Run", True, Constants.WHITE)

        self.player_nitzamon_name = self.font.render(f"Name: {self.equipped_player_nitzamon.name}", True, Constants.BLACK)
        self.player_nitzamon_hp = self.font.render("HP: ", True, Constants.BLACK)
        self.player_nitzamon_lvl = self.font.render(f"Level: {self.equipped_player_nitzamon.lvl}", True, Constants.BLACK)

        self.enemy_nitzamon_name = self.font.render(f"Name: {self.equipped_enemy_nitzamon.name}", True, Constants.BLACK)
        self.enemy_nitzamon_hp = self.font.render("HP: ", True, Constants.BLACK)
        self.enemy_nitzamon_lvl = self.font.render(f"Level: {self.equipped_enemy_nitzamon.lvl}", True, Constants.BLACK)

    def draw_screen(self):
        self.change_info()
        Constants.WIN.fill((0, 255, 0))
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.main_rect)
        pygame.draw.rect(Constants.WIN, self.fight_rect_color, self.topLeft_rect)
        pygame.draw.rect(Constants.WIN, self.inventory_rect_color, self.topRight_rect)
        pygame.draw.rect(Constants.WIN, self.catch_rect_color, self.bottomLeft_rect)
        pygame.draw.rect(Constants.WIN, self.run_rect_color, self.bottomRight_rect)
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

        Constants.WIN.blit(self.enemy_nitzamon_name,
                           (self.enemy_nitzamon_info.x + 10, self.enemy_nitzamon_info.y + 10))

        Constants.WIN.blit(self.enemy_nitzamon_hp,
                           (self.enemy_nitzamon_info.x + 10,
                            self.enemy_nitzamon_info.y + 20 + Constants.FIGHT_FONT_SIZE))
        Constants.WIN.blit(self.enemy_nitzamon_lvl,
                           (self.enemy_nitzamon_info.x + 10,
                            self.enemy_nitzamon_info.y + 30 + 2 * Constants.FIGHT_FONT_SIZE))

        player_nitzamon_sprite = pygame.transform.scale(self.equipped_player_nitzamon.sprite, (200, 200))
        enemy_nitzamon_sprite = pygame.transform.scale(self.equipped_enemy_nitzamon.sprite, (200, 200))
        Constants.WIN.blit(player_nitzamon_sprite, (100, self.player_nitzamon_info.y + 250))
        Constants.WIN.blit(enemy_nitzamon_sprite, (Constants.X - 300, self.enemy_nitzamon_info.y + 250))

    # Checking if the mouse is hovering over the buttons, if it is, the buttons will change color
    def check_hovers(self, pos):
        if self.topLeft_rect.collidepoint(pos):
            self.fight_rect_color = Constants.HOVER_COLOR
        elif self.topRight_rect.collidepoint(pos):
            self.inventory_rect_color = Constants.HOVER_COLOR
        elif self.bottomLeft_rect.collidepoint(pos):
            self.catch_rect_color = Constants.HOVER_COLOR
        elif self.bottomRight_rect.collidepoint(pos):
            self.run_rect_color = Constants.HOVER_COLOR
        else:
            self.fight_rect_color = Constants.BLACK
            self.inventory_rect_color = Constants.BLACK
            self.catch_rect_color = Constants.BLACK
            self.run_rect_color = Constants.BLACK

    def run(self, pos):
        if self.bottomRight_rect.collidepoint(pos):
            if random.randint(1, 10) == 10:
                self.in_fight = False
                self.fight_start = time.time()

    def attack(self):
        move1 = self.font.render(self.equipped_player_nitzamon.list_of_moves[0].name, True, Constants.WHITE)
        move2 = self.font.render(self.equipped_player_nitzamon.list_of_moves[1].name, True, Constants.WHITE)
        move3 = self.font.render(self.equipped_player_nitzamon.list_of_moves[2].name, True, Constants.WHITE)
        move4 = self.font.render(self.equipped_player_nitzamon.list_of_moves[3].name, True, Constants.WHITE)

        Constants.WIN.blit(move1, (self.topLeft_rect.x + 50, self.topLeft_rect.y + 5))
        Constants.WIN.blit(self.inventory_text, (self.topRight_rect.x + 30, self.topRight_rect.y + 5))
        Constants.WIN.blit(self.catch_text, (self.bottomLeft_rect.x + 50, self.bottomLeft_rect.y + 5))
        Constants.WIN.blit(self.run_text, (self.bottomRight_rect.x + 60, self.bottomRight_rect.y + 5))

    def change_nitzamons(self, new_nitzamon):
        self.equipped_player_nitzamon = new_nitzamon


    def change_info(self):
        self.player_nitzamon_name = self.font.render(f"Name: {self.equipped_player_nitzamon.name}", True, Constants.BLACK)
        self.player_nitzamon_hp = self.font.render("HP: ", True, Constants.BLACK)
        self.player_nitzamon_lvl = self.font.render(f"Level: {self.equipped_player_nitzamon.lvl}", True, Constants.BLACK)

        self.enemy_nitzamon_name = self.font.render(f"Name: {self.equipped_enemy_nitzamon.name}", True, Constants.BLACK)
        self.enemy_nitzamon_hp = self.font.render("HP: ", True, Constants.BLACK)
        self.enemy_nitzamon_lvl = self.font.render(f"Level: {self.equipped_enemy_nitzamon.lvl}", True, Constants.BLACK)

