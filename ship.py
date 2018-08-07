import pygame

class Ship():

    def __init__(self, setting, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.setting = setting

        # 存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.setting.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.centerx -= self.setting.ship_speed_factor
        if self.move_up and self.rect.top > 0:
            self.centery -= self.setting.ship_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.setting.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    