class Settings:
    """Описывает параметры экрана и мяча"""
    def __init__(self):
        """Задает начальные значения"""
        # Параметры экрана
        self.screen_width = 500
        self.screen_height = 500
        self.screen_color = 'lightyellow'

        # Параметры мяча
        self.radius = 20
        self.ball_color = 'red'
        # Скорость от min=1 до max=10
        self.ball_speed = 1
