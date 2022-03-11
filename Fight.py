import pygame
import Constants


def check_hovers(pos):
    fight_rect = pygame.Rect((905, 610), (170, 50))
    inventory_rect = pygame.Rect((1100, 610), (170, 50))
    print(f"({Constants.X}, {Constants.Y})")
    if fight_rect.collidepoint(pos):
        pygame.draw.rect(Constants.WIN, (125, 125, 125), fight_rect)
    if inventory_rect.collidepoint(pos):
        pygame.draw.rect(Constants.WIN, (125, 125, 125), inventory_rect)


