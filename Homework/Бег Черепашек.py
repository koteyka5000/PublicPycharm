import turtle
import random

size = int(input('Размер поля: '))


linecolour1 = 'black'
linecolour2 = 'white'
bgcolor = 'green'

sc = turtle.getscreen()

linet = turtle.Turtle()  # Создаём черепашек
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
turtles = (t1, t2, t3, t4)

sc.bgcolor(bgcolor)  # Цвет фона


def set_turtles():  # Ставим черепашек на место и задаём им цвет
    for q in turtles:  q.penup()
    t2.goto(0, 40)
    t3.goto(0, 80)
    t4.goto(0, 120)

    t1.color('yellow')
    t2.color('red')
    t3.color('blue')
    for q in turtles:  q.pendown()


def draw_line(size):  # Чертим разметку
    linet.up()
    linet.goto(size, 0)
    linet.down()
    linet.left(90)
    for i in range(12):
        linet.color(linecolour1)
        linet.forward(5)
        linet.color(linecolour2)
        linet.forward(5)
    linet.hideturtle()


def main(size):  # Главный процесс
    set_turtles()
    draw_line(size)
    t1x, t2x, t3x, t4x = 0, 0, 0, 0
    while t1x < size and t2x < size and t3x < size and t4x < size:
        for q in turtles:
            q.forward(random.uniform(0, 5))
            t1x = t1.xcor()
            t2x = t2.xcor()
            t3x = t3.xcor()
            t4x = t4.xcor()
    get_winner(t1x, t2x, t3x, t4x)


def get_winner(t1x, t2x, t3x, t4x):  # Отображаем победителя
    mtx = max(t1x, t2x, t3x, t4x)
    if t1x == mtx:
        print('YELLOW IS WINNER')
    elif t2x == mtx:
        print('RED IS WINNER')
    elif t3x == mtx:
        print('BLUE IS WINNER')
    elif t4x == mtx:
        print('BLACK IS WINNER')


main(size)
sc.mainloop()
