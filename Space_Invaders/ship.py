import pygame

class Ship():
    def __init__(self, settings, screen):
        """Инициализация корабля и задание его начальной позиции"""
        self.screen      = screen
        self.settings    = settings
        # Загрузка изображения корабля и получение его прямоугольника
        self.image       = pygame.image.load('images/ship.bmp')
        self.rect        = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        self.center       = float(self.rect.centerx)
        # флаг перемещения
        self.moving_right = False
        self.moving_left  = False


    def blitme(self):
        """Отрисовка корабля в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    
    def update(self):
        if self.moving_right:
           #self.rect.centerx += 1
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.settings.ship_speed_factor
        
        if self.moving_left:
            #self.rect.centerx -= 1
            if self.moving_left and self.rect.left > 0:
                self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center




