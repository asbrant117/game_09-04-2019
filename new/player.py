#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *



class Player(sprite.Sprite):
    def __init__(self, x, y, all_settings,screen):
        sprite.Sprite.__init__(self)
        self.all_settings = all_settings
        self.screen = screen
        self.X = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.Y = y
        self.image = Surface((40, 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = Rect(x, y, 40, 40)  # прямоугольный объект
        self.image.set_colorkey((255, 255, 255))  # делаем фон прозрачным

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        if self.moving_right:
            self.X += self.all_settings.hero_speed
        if self.moving_left:
            self.X -= self.all_settings.hero_speed
        if self.moving_up:
            self.Y -= self.all_settings.hero_speed
        if self.moving_down:
            self.Y += self.all_settings.hero_speed

    def blitme(self):
        self.screen.blit( pygame.image.load('pic/test.png'), (0,0))