import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, settings, screen, ship, bullets):
    # обработка нажатия клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # создание новой пули и добавление в группу
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    # обработка отпускания клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, ship, bullets):
    # отслеживание событий клавиатуры и мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets):
        # при каждом проходе цикла перерисовывается экран
        screen.fill(settings.bg_color)
        # все пули рисуются поверх экрана
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        # отображение последнего прорисованного экрана
        pygame.display.flip()
