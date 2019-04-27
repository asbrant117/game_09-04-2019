import pygame
import animation


class Game_character(pygame.sprite.Sprite, animation.Animation):
    def __init__(self, all_settings, screen, hero, x, y):
        # родительские классы
        pygame.sprite.Sprite.__init__(self)
        animation.Animation.__init__(self)
        # инициализирует персонажа и поверхность
        self.screen = screen
        self.all_settings = all_settings
        self.screen = screen
        self.hero = hero

        # изображение героя и выделенный прямоугольник
        self.image = self.animation_character_stay_down  #
        self.rect = pygame.Rect(x,
                                y, 80, 90)

        self.rect.x = x
        self.rect.y = y

        # сохранение точной позиции
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = all_settings.bullet_color

        # состояние уворота
        self.dodge = False

    # перемещение персонажа
    def update_character(self, bullets_left):
        # выбор движения (уворт или идти к герою)
        if self.dodge == False:
            # формула для вычисления растояние до героя
            distance = ((self.hero.rect.x - self.x) ** 2 + (self.hero.rect.y - self.y) ** 2) ** 0.5
            distance2 = ((self.hero.rect.x - self.x - self.all_settings.character_speed) ** 2 + (
                    self.hero.rect.y - self.y) ** 2) ** 0.5
            distance3 = ((self.hero.rect.x - self.x + self.all_settings.character_speed) ** 2 + (
                    self.hero.rect.y - self.y) ** 2) ** 0.5
            distance4 = ((self.hero.rect.x - self.x) ** 2 + (
                    self.hero.rect.y - self.y - self.all_settings.character_speed) ** 2) ** 0.5
            distance5 = ((self.hero.rect.x - self.x) ** 2 + (
                    self.hero.rect.y - self.y + self.all_settings.character_speed) ** 2) ** 0.5
            if distance2 < distance:
                # передвижение персонажа
                self.x += self.all_settings.character_speed
                # сохранение координат
                self.rect.x = self.x
            if distance3 < distance:
                # передвижение персонажа
                self.x -= self.all_settings.character_speed
                # сохранение координат
                self.rect.x = self.x
            if distance4 < distance:
                # передвижение персонажа
                self.y += self.all_settings.character_speed
                # сохранение координат
                self.rect.y = self.y
            if distance5 < distance:
                # передвижение персонажа
                self.y -= self.all_settings.character_speed
                # сохранение координат
                self.rect.y = self.y
        # перебераем все пули и сравниваем, успеет ли персонаж от нее увернутся
        for bullet_left in bullets_left:
            t_bull = abs(self.x - bullet_left.x + 80) / self.all_settings.bullet_speed_factor
            t_char = abs(100 - abs(self.y - bullet_left.y)) / self.all_settings.character_speed
            # если есть опасность и персонаж успевает увернутся, то персонаж уворачивается
            if (bullet_left.y < self.y + 120) and (bullet_left.y > self.y - 10) and (bullet_left.x > self.x) and (
                    t_bull > t_char):
                self.dodge = True
                #    d1 = ((bullet_left.x - self.x) ** 2 + (bullet_left.y - self.y ) ** 2) ** 0.5
                #    d2 = ((bullet_left.x - self.x) ** 2 + (bullet_left.y - self.y - 50) ** 2) ** 0.5
                # передвижение персонажа
                self.y -= self.all_settings.character_speed
                # сохранение координат
                self.rect.y = self.y
            else:
                self.dodge = False

    #
    def blit_character(self):
        self.frame = 0
        self.screen.blit(self.image[int(self.frame)], self.rect)
