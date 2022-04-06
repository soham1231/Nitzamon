import Main
import MainMenu
import pygame
from Constants import X, Y

print(X, Y)

pygame.init()


main_menu = MainMenu.MainMenu()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_menu.play_rect.collidepoint(pygame.mouse.get_pos()):
                run = Main.main()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
    main_menu.draw()
    main_menu.check_hover(pygame.mouse.get_pos())

    pygame.display.update()
pygame.quit()
