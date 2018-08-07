import sys
import pygame

from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
    pygame.display.init()

    settings = Setting()
    bullets = Group()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)

    # 主循环
    while True:
        
        gf.check_events(screen,settings,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(screen,settings,ship,bullets)

run_game()