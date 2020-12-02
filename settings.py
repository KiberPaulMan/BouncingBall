import ball_movement as bm


class Settings:
    """Описывает параметры экрана и мяча"""
    def __init__(self):
        """Задает начальные значения"""
        # Параметры экрана
        self.screen_width = 450
        self.screen_height = 450
        self.screen_color = 'lightyellow'

        # Параметры мяча
        self.radius = 20
        self.ball_color = 'red'
        # Скорость от min=1 до max=10
        self.ball_speed = 20
        # Начальный угол
        self.angle = bm.random_angle()

        # Границы экрана по осям x и y
        self.l_board_x = self.radius/2 - int(self.screen_width / 2)
        self.r_board_x = int(self.screen_width / 2) - self.radius

        self.b_board_y = self.radius - int(self.screen_height / 2)
        self.t_board_y = int(self.screen_height / 2) - self.radius/2