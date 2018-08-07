import sys

import pygame
from bullet import Bullet

def check_keydown_event(event,screen,settings,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False

def check_events(screen,settings,ship,bullets):
    # 监听键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,screen,settings,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(screen, settings, ship, bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
    
