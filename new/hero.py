import pygame
import animation


class Hero(pygame.sprite.Sprite, animation.Animation):
    def __init__(self, all_settings, screen):
        pygame.sprite.Sprite.__init__(self)
        animation.Animation.__init__(self)
        # инициализирует героя и поверхность
        self.screen = screen
        self.all_settings = all_settings

        # данные времени для анимации
        self.time = all_settings.time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

        # изображение героя и выделенный прямоугольник
        self.image = self.animation_hero_stay_down  #
        self.rect = pygame.Rect(self.all_settings.x, self.all_settings.y, 38, 70)

        # координаты расположения
        self.rect.x = self.all_settings.x
        self.rect.y = self.all_settings.y

        # флажки перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # флажок направления
        self.direction = 'down'

        # сохранение координат коробля
        self.center = float(self.rect.x)
        self.bottom = float(self.rect.y)

    # Функция помогающая отслеживать перемещение
    def update_hero(self, dt):
        if self.moving_right:
            self.center += self.all_settings.hero_speed
            self.direction = 'right'
        if self.moving_left:
            self.center -= self.all_settings.hero_speed
            self.direction = 'left'
        if self.moving_up:
            self.bottom -= self.all_settings.hero_speed
            self.direction = 'up'
        if self.moving_down:
            self.bottom += self.all_settings.hero_speed
            self.direction = 'down'

        # время жизни кадра
        self.work_time += dt
        self.skip_frame = self.work_time / self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.work_time
            self.frame += self.skip_frame
            if self.frame >= len(self.image):
                self.frame = 0

        # передаем изменения
        self.rect.x = self.center
        self.rect.y = self.bottom

    # отображение героя
    def blit_hero(self):
        if self.moving_right:
            self.image = self.animation_hero_right
        elif self.moving_left:
            self.image = self.animation_hero_left
        elif self.moving_up:
            self.image = self.animation_hero_up
        elif self.moving_down:
            self.image = self.animation_hero_down
        else:
            if self.direction == 'down':
                self.image = self.animation_hero_stay_down
            elif self.direction == 'left':
                self.image = self.animation_hero_stay_left
            elif self.direction == 'right':
                self.image = self.animation_hero_stay_right
            elif self.direction == 'up':
                self.image = self.animation_hero_stay_up

        self.screen.blit(self.image[int(self.frame)], self.rect)
