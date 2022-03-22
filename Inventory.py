import Constants
import pygame
from math import ceil


is_open = False
info_open = False
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
        if i != 0:
            y_min = 40 + i * nitzamon_img_scale
            y_max = nitzamon_img_scale + 40 + i * nitzamon_img_scale
        else:
            y_min = 40
            y_max = 40 + nitzamon_img_scale
        for j in range(len(nitzamons[i])):
            if j != 0:
                x_min = 40 + j * nitzamon_img_scale
                x_max = nitzamon_img_scale + 40 + j * nitzamon_img_scale
            else:
                x_min = 40
                x_max = 40 + nitzamon_img_scale
            if y_min <= pos[1] <= y_max and x_min <= pos[0] <= x_max:
                return nitzamons[i][j]
    return None


def show_info(nitzamon):
    info_img_x = 500
    info_img_y = 50
    Constants.WIN.fill(Constants.GREY)
    info_img = pygame.image.load("Assets\\Menus\\NitzamonDisplay.png")
    Constants.WIN.blit(info_img, (info_img_x, info_img_y))
    nitzamon_image = pygame.transform.scale(nitzamon.sprite, (290, 388))
    Constants.WIN.blit(nitzamon_image, (info_img_x + 30, info_img_y + 28))
