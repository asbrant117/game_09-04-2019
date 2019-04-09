import pygame
from animation import Animation


class Hero():
    def __init__(self, all_settings, screen):
        # инициализирует героа и задает его начальную позицию
        self.screen = screen
        self.all_settings = all_settings

        # изображение коробля и выделяем прямоугольник
        self.image = pygame.image.load('pic/test.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # сохраняем прямоугольник героя

        # координаты расположения
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # флажки перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # сохранение координат коробля
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    # Функция помогающая отслеживать перемещение
    def update(self):
        if self.moving_right:
            self.center += self.all_settings.hero_speed
        if self.moving_left:
            self.center -= self.all_settings.hero_speed
        if self.moving_up:
            self.bottom -= self.all_settings.hero_speed
        if self.moving_down:
            self.bottom += self.all_settings.hero_speed

        # передаем изменения
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    # отображение героя
    def blitme(self):
        self.screen.blit(self.image, self.rect)
