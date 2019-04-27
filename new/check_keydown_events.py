import sys
import pygame
from bullet import Bullet


# обработка нажатий клафиш
def check_keydown_events(event, all_settings, screen, hero, bullets_right, bullets_left, bullets_up, bullets_down):
    # передвижение
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        hero.moving_right = True
        hero.moving_left = hero.moving_down = hero.moving_up = False
        hero.direction = 'right'

    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        hero.moving_left = True
        hero.moving_down = hero.moving_right = hero.moving_up = False
        hero.direction = 'left'

    if event.key == pygame.K_UP or event.key == pygame.K_w:
        hero.moving_up = True
        hero.moving_right = hero.moving_left = hero.moving_down = False
        hero.direction = 'up'

    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        hero.moving_down = True
        hero.moving_right = hero.moving_left = hero.moving_up = False
        hero.direction = 'down'

    # стрельба
    if event.type == pygame.K_SPACE or event.key == pygame.K_e:
        if len(bullets_right) + len(bullets_left) + len(bullets_up) + len(
                bullets_down) < all_settings.bullet_allowed:  # ?
            # ооздаем 4 группы пуль (на каждую сторону координаст) и добавляем в список при нажатии
            if hero.direction == 'up':
                new_bullet_up = Bullet(all_settings, screen, hero,
                                       all_settings.bullet_width, all_settings.bullet_height)
                bullets_up.add(new_bullet_up)
            if hero.direction == 'right':
                new_bullet_right = Bullet(all_settings, screen, hero,
                                          all_settings.bullet_height, all_settings.bullet_width)
                bullets_right.add(new_bullet_right)
            if hero.direction == 'left':
                new_bullet_left = Bullet(all_settings, screen, hero,
                                         all_settings.bullet_height, all_settings.bullet_width)
                bullets_left.add(new_bullet_left)
            if hero.direction == 'down':
                new_bullet_down = Bullet(all_settings, screen, hero,
                                         all_settings.bullet_width, all_settings.bullet_height)
                bullets_down.add(new_bullet_down)
    # выход из игры
    if event.key == pygame.K_ESCAPE:
        sys.exit()

