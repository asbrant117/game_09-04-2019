import sys
import pygame
from time import sleep
from Сheck_keydown_events import check_keydown_events
from Check_keyup_events import check_keyup_events




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




def update_screen(all_settings, screen, hero, bullets, bullets_right, bullets_left, bullets_up, bullets_down,
                  characters):
    # перерисовка
    # экран
    screen.fill(all_settings.screen_color)
    # герой
    hero.blit_hero()



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
  # for bullet_left in  bullets_left:
  #     if bullet_left.rect.x <= 20:
  #         bullets_left.remove(bullet_left)

    # регистрация попадания
    #collision =
    collision = pygame.sprite.groupcollide(bullets_down, characters, True, True)
    collision = pygame.sprite.groupcollide(bullets_up, characters, True, True)
    collision = pygame.sprite.groupcollide(bullets_left, characters, True, True)
    collision = pygame.sprite.groupcollide(bullets_right, characters, True, True)

    # персонаж
    for character in characters.sprites():
        character.blit_character()
      #  character.update_character(bullets_left)


    if pygame.sprite.spritecollideany(hero,characters):
        print('столкновение')
        sleep(0.2)

    # отображение последнего прорисованного экрана
    pygame.display.flip()
