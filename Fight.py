import time

import pygame
import Constants
import random


class FightMenu:
    def __init__(self, player_nitzamons, enemy_nitzamons):

        self.player_nitzamons = player_nitzamons
        self.enemy_nitzamons = enemy_nitzamons

        self.equipped_player_nitzamon = self.player_nitzamons[0]
        self.equipped_enemy_nitzamon = self.enemy_nitzamons[0]

        self.in_fight = False
        self.fight_start = time.time()

        self.main_rect = pygame.Rect((0, Constants.Y - 250), (Constants.X, 250))
        self.fight_rect = pygame.Rect((Constants.X - 500, Constants.Y - 200), (170, 50))
        self.inventory_rect = pygame.Rect((Constants.X - 250, Constants.Y - 200), (170, 50))
        self.catch_rect = pygame.Rect((Constants.X - 500, Constants.Y - 100), (170, 50))
        self.run_rect = pygame.Rect((Constants.X - 250, Constants.Y - 100), (170, 50))

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
        pygame.draw.rect(Constants.WIN, self.fight_rect_color, self.fight_rect)
        pygame.draw.rect(Constants.WIN, self.inventory_rect_color, self.inventory_rect)
        pygame.draw.rect(Constants.WIN, self.catch_rect_color, self.catch_rect)
        pygame.draw.rect(Constants.WIN, self.run_rect_color, self.run_rect)
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.enemy_nitzamon_info)
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.player_nitzamon_info)

        Constants.WIN.blit(self.fight_text, (self.fight_rect.x + 50, self.fight_rect.y + 5))
        Constants.WIN.blit(self.inventory_text, (self.inventory_rect.x + 30, self.inventory_rect.y + 5))
        Constants.WIN.blit(self.catch_text, (self.catch_rect.x + 50, self.catch_rect.y + 5))
        Constants.WIN.blit(self.run_text, (self.run_rect.x + 60, self.run_rect.y + 5))

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
        if self.fight_rect.collidepoint(pos):
            self.fight_rect_color = Constants.HOVER_COLOR
        elif self.inventory_rect.collidepoint(pos):
            self.inventory_rect_color = Constants.HOVER_COLOR
        elif self.catch_rect.collidepoint(pos):
            self.catch_rect_color = Constants.HOVER_COLOR
        elif self.run_rect.collidepoint(pos):
            self.run_rect_color = Constants.HOVER_COLOR
        else:
            self.fight_rect_color = Constants.BLACK
            self.inventory_rect_color = Constants.BLACK
            self.catch_rect_color = Constants.BLACK
            self.run_rect_color = Constants.BLACK

    def run(self, pos):
        if self.run_rect.collidepoint(pos):
            if random.randint(1, 10) == 10:
                self.in_fight = False
                self.fight_start = time.time()

    def change_nitzamons(self, p, e):
        # Checking if the current nitzamon is the player's equipped nitzamon
        for i in range(len(self.player_nitzamons)):
            if self.player_nitzamons[i] == p.equipped_nitzamon:
                self.equipped_player_nitzamon = self.player_nitzamons[i]

        # Checking if the current nitzamon is the enemy's equipped nitzamon
        for i in range(len(self.enemy_nitzamons)):
            if self.enemy_nitzamons[i] == e.equipped_nitzamon:
                self.equipped_enemy_nitzamon = self.enemy_nitzamons[i]

    def change_info(self):
        self.player_nitzamon_name = self.font.render(f"Name: {self.equipped_player_nitzamon.name}", True, Constants.BLACK)
        self.player_nitzamon_hp = self.font.render("HP: ", True, Constants.BLACK)
        self.player_nitzamon_lvl = self.font.render(f"Level: {self.equipped_player_nitzamon.lvl}", True, Constants.BLACK)

        self.enemy_nitzamon_name = self.font.render(f"Name: {self.equipped_enemy_nitzamon.name}", True, Constants.BLACK)
        self.enemy_nitzamon_hp = self.font.render("HP: ", True, Constants.BLACK)
        self.enemy_nitzamon_lvl = self.font.render(f"Level: {self.equipped_enemy_nitzamon.lvl}", True, Constants.BLACK)
