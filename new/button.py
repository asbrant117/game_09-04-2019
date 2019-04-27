import pygame.font

class Button():
    def __init__(self,all_settings, screen,msg):
        self.screen = screen
        self.all_settings = all_settings

        #размеры и свойства кнопки
        self.width,self.heught = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)