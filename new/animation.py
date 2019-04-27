import pygame

ANIMATION_DOWN = [(0, 0, 50, 64), (50, 0, 45, 64), (96, 0, 45, 64), (146, 0, 45, 64)]
ANIMATION_LEFT = [(0, 64, 50, 64), (50, 64, 44, 64), (96, 64, 50, 64), (146, 64, 45, 64)]
ANIMATION_RIGHT = [(0, 128, 48, 64), (50, 128, 43, 64), (96, 128, 44, 64), (146, 128, 44, 64)]
ANIMATION_UP = [(0, 192, 48, 64), (50, 192, 43, 64), (96, 192, 43, 64), (146, 192, 45, 64)]

ANIMATION_STAY_DOWN = [(0, 0, 50, 64), (0, 0, 50, 64), (0, 0, 50, 64), (0, 0, 50, 64)]
ANIMATION_STAY_LEFT = [(0, 64, 50, 64), (0, 64, 50, 64), (0, 64, 50, 64), (0, 64, 50, 64)]
ANIMATION_STAY_RIGHT = [(0, 128, 48, 64), (0, 128, 48, 64), (0, 128, 48, 64), (0, 128, 48, 64)]
ANIMATION_STAY_UP = [(0, 192, 48, 64), (0, 192, 48, 64), (0, 192, 48, 64), (0, 192, 48, 64)]

ANIMATION_CHARACTER_STAY = [(0, 0, 100, 100), (0, 0, 100, 100), (0, 0, 100, 100), (0, 0, 100, 100)]


class Animation():
    def __init__(self):
        self.sprite_hero = pygame.image.load('pic/pic/ryuk.png').convert_alpha()
        self.sprite_character = pygame.image.load('pic/pic/bahamut.png').convert_alpha()

        # персонаж
        anim = []
        for frame in ANIMATION_CHARACTER_STAY:
            anim.append(self.sprite_character.subsurface(frame))
        self.animation_character_stay_down = anim

        # герой
        # вниз
        anim = []
        for frame in ANIMATION_STAY_DOWN:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_stay_down = anim

        anim = []
        for frame in ANIMATION_DOWN:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_down = anim

        # налево
        anim = []
        for frame in ANIMATION_STAY_LEFT:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_stay_left = anim

        anim = []
        for frame in ANIMATION_LEFT:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_left = anim

        # направо
        anim = []
        for frame in ANIMATION_STAY_RIGHT:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_stay_right = anim

        anim = []
        for frame in ANIMATION_RIGHT:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_right = anim

        # вверх
        anim = []
        for frame in ANIMATION_STAY_UP:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_stay_up = anim

        anim = []
        for frame in ANIMATION_UP:
            anim.append(self.sprite_hero.subsurface(frame))
        self.animation_hero_up = anim
