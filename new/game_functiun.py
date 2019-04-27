import sys
import pygame
from bullet import Bullet
from game_character import Game_character
import random
from time import sleep

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


# события отжатия клваиш
def check_keyup_events(event, hero):
    # передвижение (регестрация отжатия клафиши)
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        hero.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        hero.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        hero.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        hero.moving_down = False


def check_events(all_settings, screen, hero, bullets_right, bullets_left, bullets_up, bullets_down):
    # обработка действий
    for event in pygame.event.get():
        # выход
        if event.type == pygame.QUIT:
            sys.exit()
        # регистрация нажатия
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, all_settings, screen, hero,
                                 bullets_right, bullets_left, bullets_up, bullets_down)
        # регистрация отжатия
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


def create_chatacters(all_settings, screen, characters):
    # chatacter = Game_character(all_settings,screen)
    # chatacter_width = chatacter.rect.x
    # for chatacter_number in range(8):
    #    chatacter = Game_character(all_settings, screen)
    #    chatacter.x = chatacter.rect.x + chatacter_width*15*chatacter_number
    #    chatacter.rect.x = chatacter.x
    #    chatacter.rect.y = chatacter.y
    #    characters.add(chatacter)

    coordinates = ((50, 50), (200, 50), (600, 50), (50, 150),
                   (180, 200), (400, 450), (1000, 500))

    for coordinate in coordinates:
        chatacter = Game_character(all_settings, screen)
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        chatacter.rect.x = coordinate[0] + x
        chatacter.rect.y = coordinate[1] + y
        characters.add(chatacter)


def update_screen(all_settings, screen, hero, bullets, bullets_right, bullets_left, bullets_up, bullets_down,
                  characters):
    # перерисовка
    # экран
    screen.fill(all_settings.screen_color)
    # герой
    hero.blit_hero()

    # персонаж
    for character in characters.sprites():
        character.blit_character()

    # пули
    for bullet_right in bullets_right.sprites():
        bullet_right.update_bul_right()
        bullet_right.blit_bullet()

    for bullet_left in bullets_left.sprites():
        bullet_left.update_bul_left()
        bullet_left.blit_bullet()

    for bullet_up in bullets_up.sprites():
        bullet_up.update_bul_up()
        bullet_up.blit_bullet()

    for bullet_down in bullets_down.sprites():
        bullet_down.update_bul_down()
        bullet_down.blit_bullet()

    # удаление лишних пуль #вопрос, как работать с группой?
    for bullet in bullets:
        if bullet.rect.y <= 0 or bullet.rect.y >= all_settings.screen_height:
            bullet.remove(bullet)
        if bullet.rect.x <= 0 or bullet.rect.x >= all_settings.screen_width:
            bullet.remove(bullet)

    # регистрация попадания
    #collision =
    collision = pygame.sprite.groupcollide(bullets_down, characters, True, True)
    collision = pygame.sprite.groupcollide(bullets_up, characters, True, True)
    collision = pygame.sprite.groupcollide(bullets_left, characters, True, True)
    collision = pygame.sprite.groupcollide(bullets_right, characters, True, True)
    # отображение последнего прорисованного экрана
    if pygame.sprite.spritecollideany(hero,characters):
        print('столкновение')
        sleep(0.2)
    pygame.display.flip()
