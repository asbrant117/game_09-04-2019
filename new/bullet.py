import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, all_settings, screen, hero, width, height):
        # создаем объект пули в текущей позиции героя
        super(Bullet, self).__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # создания пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, width,
                                height)
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top

        # координаты пули хранятся в вещественном формате
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = all_settings.bullet_color
        self.speed_factor = all_settings.bullet_speed_factor

    def update_bul_up(self):
        # передвижение пули
        self.y -= self.speed_factor
        # обновление позиции прямоугольника
        self.rect.y = self.y


    def update_bul_down(self):
        # передвижение пули
        self.y += self.speed_factor
        # обновление позиции прямоугольника
        self.rect.y = self.y


    def update_bul_left(self):
        # передвижение пули
        self.x -= self.speed_factor
        # обновление позиции прямоугольника
        self.rect.x = self.x


    def update_bul_right(self):
        # передвижение пули
        self.x += self.speed_factor
        # обновление позиции прямоугольника
        self.rect.x = self.x


    def blit_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
