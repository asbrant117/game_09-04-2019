import  sys
import pygame
from bullet import Bullet


#обработка нажатий клафиш
def check_keydown_events(event,all_settings,screen,hero,bullets):
    #передвижение
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        hero.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        hero.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        hero.moving_up = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        hero.moving_down = True

    if event.type == pygame.K_SPACE or event.key == pygame.K_e:
        # создаем новую пулю и включаем в список
        new_bullet = Bullet(all_settings, screen, hero)
        bullets.add(new_bullet)

def check_keyup_events(event,hero):
    # передвижение (что бы остановился)
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        hero.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        hero.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        hero.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        hero.moving_down = False


def check_events(all_settings,screen,hero,bullets):
    # обработка действий
    for event in pygame.event.get():
        # активная клафиша выхода
        if event.type == pygame.QUIT:
            sys.exit()
        #регистрация нажатия
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,all_settings,screen,hero,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


def update_screen(all_settings,screen,hero,bullets):
    # перерисовка


    screen.fill(all_settings.screen_color)
    hero.blit_hero()
    for bullet in bullets.sprites():
        bullet.update_bul()
        bullet.blit_bullet()

    # отображение последнего прорисованного экрана
    pygame.display.flip()