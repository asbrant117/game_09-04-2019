import pygame


ANIMATION_RUN = [(0, 0, 90, 64),(104, 0, 90, 64)]
ANIMATION_STAY = [(0, 0, 90, 64),(0, 0, 90, 64)]




class Animation():
    def __init__(self):
        self.sprite = pygame.image.load('svin.png').convert_alpha()

        anim =[]
        for frame in ANIMATION_STAY:
            anim.append(self.sprite.subsurface(frame))
        self.animation_hero_stay = anim

        anim = []
        for frame in ANIMATION_RUN:
            anim.append(self.sprite.subsurface(frame))
        self.animation_hero_run = anim

