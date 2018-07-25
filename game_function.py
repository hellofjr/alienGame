import sys

import pygame


def check_events(ship):
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #向右移动飞船
                ship.move_right = True
            elif event.key == pygame.K_LEFT:
                ship.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False
            elif event.key == pygame.K_LEFT:
                ship.move_left = False


def update_screen(screen, setting, ship):
    screen.fill(setting.bg_color)
    ship.blitme()
    pygame.display.flip()
    
