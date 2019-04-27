class Settings():
    # класс для хранения всех настроик игры
    def __init__(self):
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)

        # параметры времени
        self.dt = 0
        # колличество циклов while = кадрам игры в секунду
        self.fps = 60
        # время жизни отдельного карда
        self.time = 250

        # параметры героя
        # скорость
        self.hero_speed = 2.5

        # начальные координаты
        self.x = 580
        self.y = 380

        # параметры пули
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 1000  # ?

        # персонаж
        self.character_x = 10
        self.character_y = 10
        self.character_speed_factor = 1