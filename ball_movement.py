from random import randint


def random_position(st):
    """Генерирует начальную позицию мяча"""
    board_x = int(st.screen_width/2)
    board_y = int(st.screen_height/2)
    x = randint(st.radius - board_x, board_x - st.radius + 1)
    y = randint(st.radius - board_y, board_y - st.radius + 1)
    return float(x), float(y)
