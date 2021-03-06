import Constants
import pygame
from math import ceil


is_open = False
info_open = False
equip_open = False

inventory_rect = pygame.Rect((30, 30), (Constants.X - 60, Constants.Y - 60))

info_rect_width = 350
info_rect_height = 700
info_rect_x = Constants.X / 2 - info_rect_width / 2
info_rect_y = Constants.Y / 2 - info_rect_height / 2
info_rect = pygame.Rect((info_rect_x, info_rect_y), (info_rect_width, info_rect_height))

equip_rect_x = inventory_rect.width - 160
equip_rect_y = inventory_rect.height - 60
equip_rect = pygame.Rect((equip_rect_x, equip_rect_y), (150, 50))

remove_rect_x = inventory_rect.width - 170 - equip_rect.width
remove_rect_y = inventory_rect.height - 60
remove_rect = pygame.Rect((remove_rect_x, remove_rect_y), (150, 50))

pygame.font.init()
font = pygame.font.SysFont("Arial", 20)

nitzamon_img_scale = 100
cols_of_nitzamons = ceil(inventory_rect.width / (nitzamon_img_scale + 10))
rows_of_nitzamons = ceil(inventory_rect.height / (nitzamon_img_scale + 10))


def turn_into_img_matrix(inv):
    nitzamons = []
    if len(inv) >= cols_of_nitzamons:
        cols = cols_of_nitzamons
    else:
        cols = len(inv)
    if cols != 0:
        rows = ceil(len(inv) / cols)
    else:
        rows = 1
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
    Constants.WIN.fill(Constants.GREY)
    pygame.draw.rect(Constants.WIN, Constants.WHITE, info_rect)
    pygame.draw.rect(Constants.WIN, (0, 0, 255), equip_rect)
    pygame.draw.rect(Constants.WIN, (255, 0, 0), remove_rect)

    name = font.render(f"Name: {nitzamon.name}", True, Constants.BLACK)
    Constants.WIN.blit(name, (info_rect_x + 10, info_rect_y + 500))

    hp = font.render(f"Hp: {nitzamon.hp} / {nitzamon.max_hp}", True, Constants.BLACK)
    Constants.WIN.blit(hp, (info_rect_x + 10, info_rect_y + 530))

    lvl = font.render(f"Level: {nitzamon.lvl}", True, Constants.BLACK)
    Constants.WIN.blit(lvl, (info_rect_x + 10, info_rect_y + 560))

    element = font.render(f"Element: {nitzamon.element}", True, Constants.BLACK)
    Constants.WIN.blit(element, (info_rect_x + 10, info_rect_y + 590))

    attack = font.render(f"Attack: {nitzamon.dmg}", True, Constants.BLACK)
    Constants.WIN.blit(attack, (info_rect_x + 10, info_rect_y + 620))

    speed = font.render(f"Speed: {nitzamon.spd}", True, Constants.BLACK)
    Constants.WIN.blit(speed, (info_rect_x + 10, info_rect_y + 650))

    replace = font.render("Replace", True, Constants.BLACK)
    Constants.WIN.blit(replace, (equip_rect_x + 45, equip_rect_y + 10))

    delete = font.render("Delete", True, Constants.BLACK)
    Constants.WIN.blit(delete, (remove_rect_x + 50, remove_rect_y + 10))

    nitzamon_image = pygame.transform.scale(nitzamon.sprite, (290, 388))
    Constants.WIN.blit(nitzamon_image, (info_rect_x + 30, info_rect_y + 50))

    pygame.draw.line(Constants.WIN, (0, 0, 0), (info_rect_x, info_rect_y + 490), (info_rect_x + info_rect_width, info_rect_y + 490), 5)
