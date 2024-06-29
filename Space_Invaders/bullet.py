import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        """создание пули и задание ее позиции"""
        super(Bullet, self).__init__()
        self.screen = screen
        # создание пули и задание ее позиции
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # сохранение позиции пули
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor


    def update(self):
        # перемещение пули
        self.y -= self.speed_factor
        # обновление позиции пули
        self.rect.y = self.y


    def draw_bullet(self):
        # отрисовка пули
        pygame.draw.rect(self.screen, self.color, self.rect)