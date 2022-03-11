import pygame
import Constants


def check_hovers(pos):
    fight_rect = pygame.Rect((Constants.X - 500, Constants.Y - 200), (170, 50))
    inventory_rect = pygame.Rect((Constants.X - 250, Constants.Y - 200), (170, 50))
    catch_rect = pygame.Rect((Constants.X - 500, Constants.Y - 100), (170, 50))
    run_rect = pygame.Rect((Constants.X - 250, Constants.Y - 100), (170, 50))
    print(f"({Constants.X}, {Constants.Y})")
    fight_rect_color = (0, 0, 0)
    inventory_rect_color = (0, 0, 0)
    catch_rect_color = (0, 0, 0)
    run_rect_color = (0, 0, 0)
    if fight_rect.collidepoint(pos):
        fight_rect_color = (125, 125, 125)
    elif inventory_rect.collidepoint(pos):
        inventory_rect_color = (125, 125, 125)
    elif catch_rect.collidepoint(pos):
        catch_rect_color = (125, 125, 125)
    elif run_rect.collidepoint(pos):
        run_rect_color = (125, 125, 125)
    else:
        fight_rect_color = (0, 0, 0)
        inventory_rect_color = (0, 0, 0)
        catch_rect_color = (0, 0, 0)
        run_rect_color = (0, 0, 0)

    pygame.draw.rect(Constants.WIN, fight_rect_color, fight_rect)
    pygame.draw.rect(Constants.WIN, inventory_rect_color, inventory_rect)
    pygame.draw.rect(Constants.WIN, catch_rect_color, catch_rect)
    pygame.draw.rect(Constants.WIN, run_rect_color, run_rect)


