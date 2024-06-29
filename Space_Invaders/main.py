import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    # инициализация параметров игры и создание экрана
    settings = Settings()
    # инициализация игры и создание экрана
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    bg_color = (230, 230, 230)
    # создание корабля
    ship   = Ship(settings, screen)
    bullets = Group()


    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)


run_game()