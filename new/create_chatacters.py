import sys
import pygame
from bullet import Bullet
from game_character import Game_character
import random


# создаем по определенным критериям персонажий и добавляем в группу
def create_chatacters(all_settings, screen, characters, hero):

    # создание персонажа в определенных координатах
    while True:
        # рандомная выборка
        x = random.randint(10, 1600)
        y = random.randint(10, 900)

        # проверка на пересечение с героем
        if (x < (hero.rect.x - 200) or x > (hero.rect.x + 200)) or \
                (y < (hero.rect.y - 200) or y > (hero.rect.y + 200)):
            # создание персонажа
            character = Game_character(all_settings, screen, hero,x,y)
            character.rect.x = x
            character.rect.y = y
            # проверка на пересечение с другими персонажами
            if not pygame.sprite.spritecollideany(character, characters):
                # при отуствии пересечений с чем либо, мы добавляем в группу и выходим из цикла
                characters.add(character)
                break


#      else:
#          for character in characters:
#              if x < (character.rect.x - 200) or x > (character.rect.x + 200) or y < (
#                      character.rect.y - 200) or y > (character.rect.y + 200):
#                  character = Game_character(all_settings, screen)
#                  character.rect.x = x
#                  character.rect.y = y
#                  characters.add(character)
#                  break
