import pygame
import Constants


class FightMenu:
    def __init__(self):
        self.main_rect = pygame.Rect((0, Constants.Y - 250), (Constants.X, 250))
        self.fight_rect = pygame.Rect((Constants.X - 500, Constants.Y - 200), (170, 50))
        self.inventory_rect = pygame.Rect((Constants.X - 250, Constants.Y - 200), (170, 50))
        self.catch_rect = pygame.Rect((Constants.X - 500, Constants.Y - 100), (170, 50))
        self.run_rect = pygame.Rect((Constants.X - 250, Constants.Y - 100), (170, 50))

        self.fight_rect_color = Constants.BLACK
        self.inventory_rect_color = Constants.BLACK
        self.catch_rect_color = Constants.BLACK
        self.run_rect_color = Constants.BLACK

        self.font = pygame.font.SysFont("arial", 32)
        self.fight_text = self.font.render("Fight", True, Constants.WHITE)
        self.inventory_text = self.font.render("Inventory", True, Constants.WHITE)
        self.catch_text = self.font.render("Catch", True, Constants.WHITE)
        self.run_text = self.font.render("Run", True, Constants.WHITE)

    def draw_screen(self):
        Constants.WIN.fill((0, 255, 0))
        pygame.draw.rect(Constants.WIN, Constants.GREY, self.main_rect)
        pygame.draw.rect(Constants.WIN, self.fight_rect_color, self.fight_rect)
        pygame.draw.rect(Constants.WIN, self.inventory_rect_color, self.inventory_rect)
        pygame.draw.rect(Constants.WIN, self.catch_rect_color, self.catch_rect)
        pygame.draw.rect(Constants.WIN, self.run_rect_color, self.run_rect)

        Constants.WIN.blit(self.fight_text, (self.fight_rect.x + 50, self.fight_rect.y + 5))
        Constants.WIN.blit(self.inventory_text, (self.inventory_rect.x + 30, self.inventory_rect.y + 5))
        Constants.WIN.blit(self.catch_text, (self.catch_rect.x + 50, self.catch_rect.y + 5))
        Constants.WIN.blit(self.run_text, (self.run_rect.x + 60, self.run_rect.y + 5))

    def check_hovers(self, pos):
        if self.fight_rect.collidepoint(pos):
            self.fight_rect_color = Constants.GREY
        elif self.inventory_rect.collidepoint(pos):
            self.inventory_rect_color = Constants.GREY
        elif self.catch_rect.collidepoint(pos):
            self.catch_rect_color = Constants.GREY
        elif self.run_rect.collidepoint(pos):
            self.run_rect_color = Constants.GREY
        else:
            self.fight_rect_color = Constants.BLACK
            self.inventory_rect_color = Constants.BLACK
            self.catch_rect_color = Constants.BLACK
            self.run_rect_color = Constants.BLACK
