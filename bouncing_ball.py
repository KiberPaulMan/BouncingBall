import turtle
import ball_movement as bm
from settings import Settings

# Инициализация класса Settings
st = Settings()

# Параметры экрана
turtle.setup(st.screen_width, st.screen_height)
turtle.bgcolor(st.screen_color)

# Скрывает иконку черепахи и траекторию движения
# turtle.hideturtle()
turtle.penup()

# Отображает круг
turtle.shape('circle')  # dot(st.radius, st.ball_color)
turtle.shapesize(1)
# Задает скорость мяча
turtle.speed(st.ball_speed)

pos_x, pos_y = bm.random_position(st)
print(pos_x, pos_y)
turtle.setx(pos_x)
turtle.sety(pos_y)

# Главный цикл
turtle.mainloop()
