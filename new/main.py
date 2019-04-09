import sys #?
import pygame
from settings import Settings
from hero import  Hero
import game_functiun
from pygame.sprite import Group



def run_game():
    pygame.init()
    dt = 0
    fps = 60
    clock= pygame.time.Clock()
    time = 220



    #создаем объект настроек.
    all_settings = Settings()
    screen = pygame.display.set_mode((all_settings.screen_width,all_settings.screen_height)) #экран

    #создание героя
    hero = Hero(all_settings,screen,time)

    #создание группы для хранения пуль
    bullets = Group()


    #основной цикл
    while True:
        #события
        game_functiun.check_events(all_settings,screen,hero,bullets) #!!!!!!!!!
        hero.update_hero(dt)
        bullets.update()
        #отображение
        game_functiun.update_screen(all_settings,screen,hero,bullets)


        #счетчик времени для отображения кадра
        dt = clock.tick(fps)

run_game()