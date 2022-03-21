import Constants
import pygame
from math import ceil, floor


is_open = False
inventory_rect = pygame.Rect((30, 30), (Constants.X - 60, Constants.Y - 60))
nitzamon_img_scale = 100
cols_of_nitzamons = 1 + ceil(inventory_rect.width / (nitzamon_img_scale + 10))
rows_of_nitzamons = ceil(inventory_rect.height / (nitzamon_img_scale + 10))


def turn_into_img_matrix(inv):
    nitzamons = []
    if len(inv) >= cols_of_nitzamons:
        cols = cols_of_nitzamons
    else:
        cols = len(inv)
    rows = ceil(len(inv) / cols)
    current_nitzamon = 0
    for i in range(rows + 1):
        new_line = []
        for j in range(cols):
            if current_nitzamon >= len(inv):
                break
            new_line.append(inv[current_nitzamon])
            current_nitzamon += 1
        nitzamons.append(new_line)
    return nitzamons


def draw_inventory(inv):
    Constants.WIN.fill(Constants.BLACK)
    pygame.draw.rect(Constants.WIN, Constants.GREY, inventory_rect)
    nitzamons = turn_into_img_matrix(inv)
    for i in range(len(nitzamons)):
        for j in range(len(nitzamons[i])):
            image = pygame.transform.scale(nitzamons[i][j].sprite, (nitzamon_img_scale, nitzamon_img_scale))
            Constants.WIN.blit(image, (40 + j * nitzamon_img_scale, 40 + i * nitzamon_img_scale))


def check_collision(pos, inv):
    nitzamons = turn_into_img_matrix(inv)
    for i in range(len(nitzamons)):
        if i == 0:
            y_min = 70
            y_max = 70 + nitzamon_img_scale
        else:
            y_min = (70 + nitzamon_img_scale) * i
            y_max = (70 + 2 * nitzamon_img_scale) * i
        for j in range(len(nitzamons[i])):
            if j == 0:
                x_min = 70
                x_max = 70 + nitzamon_img_scale
            else:
                x_min = (70 + nitzamon_img_scale) * j
                x_max = (70 + 2 * nitzamon_img_scale) * j
            if y_min <= pos[1] <= y_max and x_min <= pos[0] <= x_max:
                return nitzamons[i][j]
    return None


def show_info(nitzamon):
    info_img = pygame.image.load("Assets\\Menus\\NitzamonDisplay.png")
    Constants.WIN.blit(info_img, (100, 50))
    Constants.WIN.blit(nitzamon.sprite, (50, 50))
