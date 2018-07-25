import sys
import pygame

from setting import Setting
from ship import Ship
import game_function as gf

def run_game():
    pygame.display.init()

    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # 主循环
    while True:
        
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen,setting,ship)

run_game()