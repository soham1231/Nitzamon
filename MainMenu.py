import pygame
import Constants


class MainMenu:
    def __init__(self):

        self.play_rect = pygame.Rect((Constants.X / 2 - 250, Constants.Y / 2 - 100), (500, 50))
        self.play_rect_color = Constants.WHITE
        self.font = pygame.font.SysFont("Arial", Constants.MENU_FONT_SIZE)
        self.play_text = self.font.render("Play", True, Constants.BLACK)

        self.nitzamon_font = pygame.font.SysFont("Arial", Constants.NITZAMON_FONT_SIZE)
        self.nitzamon_text = self.nitzamon_font.render("NITZAMON!!!!", True, Constants.WHITE)

    def draw(self):
        Constants.WIN.fill(Constants.BLACK)
        pygame.draw.rect(Constants.WIN, self.play_rect_color, self.play_rect)
        Constants.WIN.blit(self.play_text, (self.play_rect.x + 225, self.play_rect.y + 7))

        Constants.WIN.blit(self.nitzamon_text, (Constants.X / 2 - 150, 50))

    def check_hover(self, pos):
        if self.play_rect.collidepoint(pos):
            self.play_rect_color = Constants.GREY
        else:
            self.play_rect_color = Constants.WHITE

