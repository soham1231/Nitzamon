import Constants
import pygame
from math import ceil


is_open = False
inventory_rect = pygame.Rect((30, 30), (Constants.X - 60, Constants.Y - 60))
nitzamon_img_scale = 100
nitzamon_per_row = ceil(inventory_rect.width / (nitzamon_img_scale + 10))
nitzamon_per_col = ceil(inventory_rect.height / (nitzamon_img_scale + 10))


def draw_inventory(inv):
    Constants.WIN.fill(Constants.BLACK)
    pygame.draw.rect(Constants.WIN, Constants.GREY, inventory_rect)
    current_nitzamon = 0
    for i in range(nitzamon_per_col + 1):
        for j in range(nitzamon_per_row + 1):
            if current_nitzamon >= len(inv):
                break
            nitzamon_sprite = pygame.transform.scale(inv[current_nitzamon].sprite, (nitzamon_img_scale, nitzamon_img_scale))
            Constants.WIN.blit(nitzamon_sprite, (40 + j * nitzamon_img_scale, 40 + i * nitzamon_img_scale))
            current_nitzamon += 1