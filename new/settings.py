


class Settings ():
    #класс для хранения всех настроик игры
    def __init__(self):
        #параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230,230,230)
        #параметры героя
        #скорость
        self.hero_speed = 4.5

        #начальные координаты
        self.x=580
        self.y=380

        #начальное состояние
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #параметры пули
        self.bullet_speed_factor = 5
        self.bullet_width = 9
        self.bullet_height = 25
        self.bullet_color = (60,60,60)
