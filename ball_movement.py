from random import randint


def random_position(st):
    """Генерирует позицию мяча в пределах экрана, заданного настройками st"""
    board_x = int(st.screen_width/2)
    board_y = int(st.screen_height/2)

    x = randint(st.radius - board_x, board_x - st.radius + 1)
    y = randint(st.radius - board_y, board_y - st.radius + 1)
    return float(x), float(y)


def random_angle():
    """Генерирует направление движения в градусах"""
    return randint(1, 360)

