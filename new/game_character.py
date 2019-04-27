import pygame
import animation


class Game_character(pygame.sprite.Sprite, animation.Animation):
    def __init__(self, all_settings, screen):
        # родительские классы
        pygame.sprite.Sprite.__init__(self)
        animation.Animation.__init__(self)
        # инициализирует персонажа и поверхность
        self.screen = screen
        self.all_settings = all_settings

        # изображение героя и выделенный прямоугольник
        self.image = self.animation_character_stay_down #
        self.rect = pygame.Rect(self.all_settings.character_x,
                                self.all_settings.character_y, 90, 95)

        self.rect.x = self.all_settings.character_x
        self.rect.y = self.all_settings.character_y

        #сохранение точной позиции
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = all_settings.bullet_color
    def blit_character(self):
        self.frame = 0
        self.screen.blit(self.image[int(self.frame)], self.rect)
        #pygame.draw.rect(self.screen, self.color, self.rect)

