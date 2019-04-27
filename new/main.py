import sys  # ?
import pygame
from settings import Settings
from hero import Hero
import game_functiun
from pygame.sprite import Group


def run_game():
    pygame.init()
    # параметры времени (нужно внести в настройки)
    dt = 0
    clock = pygame.time.Clock()

    # создаем объект настроек.
    all_settings = Settings()
    # параметры экрана
    screen = pygame.display.set_mode((all_settings.screen_width, all_settings.screen_height))  # экран

    # создание героя
    hero = Hero(all_settings, screen)

    # создание группы персонажей
    characters = Group()




    # создание группы для хранения пуль
    bullets = Group()
    bullets_right = bullets.copy()  # ?
    bullets_left = bullets.copy()  # ?
    bullets_up = bullets.copy()  # ?
    bullets_down = bullets.copy()  # ?

    # основной цикл
    while True:

        # обновление песонажей
        if len(characters) == 0:
            # размещение группы персонажей
            game_functiun.create_chatacters(all_settings, screen, characters)
        # события
        game_functiun.check_events(all_settings, screen, hero, bullets_right, bullets_left, bullets_up,
                                   bullets_down)
        # обновление
        # герой
        hero.update_hero(dt)
        # группа *патрон*
        bullets.update()
        # группа персонажей
        # characters.update()

        # отображение
        game_functiun.update_screen(all_settings, screen, hero, bullets, bullets_right, bullets_left, bullets_up,
                                    bullets_down, characters)

        # счетчик времени для отображения кадра
        dt = clock.tick(all_settings.fps)


run_game()
