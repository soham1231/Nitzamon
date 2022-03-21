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
    for i in range(nitzamon_per_col):
        for j in range(nitzamon_per_row + 1):
            if current_nitzamon >= len(inv):
                break
            nitzamon_sprite = pygame.transform.scale(inv[current_nitzamon].sprite, (nitzamon_img_scale, nitzamon_img_scale))
            Constants.WIN.blit(nitzamon_sprite, (33 + j * nitzamon_img_scale, 33 + i * nitzamon_img_scale))
            current_nitzamon += 1


def check_collision(pos, inv):
    current_nitzamon = 0
    for i in range(nitzamon_per_col):
        min_y = 40 + i * nitzamon_img_scale
        max_y = 40 + i * 2 * nitzamon_img_scale
        for j in range(nitzamon_per_row + 1):
            if current_nitzamon >= len(inv):
                return None
            min_x = 40 + j * nitzamon_img_scale
            max_x = 40 + j * 2 * nitzamon_img_scale
            if min_x <= pos[0] <= max_x:
                if min_y <= pos[1] <= max_y:
                    print("HI")
                    return inv[current_nitzamon]
            current_nitzamon += 1
    return None


def show_info(nitzamon):
    info_img = pygame.image.load("Assets\\Menus\\NitzamonDisplay.png")
    Constants.WIN.blit(info_img, (100, 50))
    Constants.WIN.blit(nitzamon.sprite, (50, 50))
