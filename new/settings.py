class Settings():
    # класс для хранения всех настроик игры
    def __init__(self):
        # параметры экрана
        self.screen_width = 1800
        self.screen_height = 1000
        self.screen_color = (230, 230, 230)

        # параметры времени
        self.dt = 0
        # колличество циклов while = кадрам игры в секунду
        self.fps = 60
        # время жизни отдельного карда
        self.time = 250

        # параметры героя
        # скорость
        self.hero_speed = 4

        # начальные координаты
        self.x = 850
        self.y = 450

        # параметры пули
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 1000  # ?

        # персонаж
       # self.character_x = 100
       # self.character_y = 0
        self.character_speed = 1