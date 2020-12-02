import turtle
import ball_movement as bm
from settings import Settings

# Инициализация класса Settings
st = Settings()

# Параметры экрана
turtle.setup(st.screen_width, st.screen_height)
turtle.bgcolor(st.screen_color)

# Скрывает траекторию движения
turtle.penup()

# Отображает круг
turtle.shape('circle')
turtle.shapesize(1)

# Задает скорость мяча
# turtle.speed(st.ball_speed)

# Переход по заданным координатам
# turtle.setposition(bm.random_position(st))

# Устанавливает угол поворота относительно начального положения
turtle.setheading(st.angle)

x, y = turtle.position()
flag = True
while flag:
    if (st.l_board_x <= x <= st.r_board_x) and (st.b_board_y <= y <= st.t_board_y):
        turtle.forward(st.ball_speed)
        x, y = turtle.position()

    else:
        turtle.right(45)
        turtle.forward(st.ball_speed)
        x, y = turtle.position()


# Получает текущую позицию
# turtle.position()

# Главный цикл
turtle.mainloop()
