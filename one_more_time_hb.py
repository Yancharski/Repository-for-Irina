import turtle

# Создаем экран
screen = turtle.Screen()
screen.setup(width=600, height=400)  # Размеры экрана

# Создаем черепашку
t = turtle.Turtle()
t.speed(0)  # Устанавливаем максимальную скорость

# Настроим текстовый объект
text = "С днем рождения!"
text_size = 24
text_color = "blue"

# Нарисуем текст
t.penup()
t.color(text_color)
t.goto(-150, 0)  # Позиция текста
t.write(text, align="left", font=("Arial", text_size, "normal"))

# Закрыть окно после клика
screen.exitonclick()
