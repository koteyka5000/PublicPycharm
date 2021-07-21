import math
import turtle


class Worker:
    def __init__(self, size):
        self.size = size


class Wall(Worker):
    def draw_wall(self):
        for lol in range(4):
            turtle.forward(self.size)
            turtle.left(90)


class Roof(Worker):
    def draw_roof(self):
        t.right(45)
        t.forward(self.size / math.sqrt(2))
        t.right(90)
        t.forward(self.size / math.sqrt(2))
        t.right(135)
        t.forward(self.size)

    def go_to_place(self):
        t.left(90)
        t.forward(self.size)


class Door(Worker):
    def draw_door(self):
        for lol in range(3):
            t.forward(self.size / 4)
            t.left(90)

    def go_to_place(self):
        t.left(90)
        t.forward(self.size)
        t.left(90)
        t.forward(self.size // 2)
        t.left(90)


s = int(input('Введите размер стен: '))
screen = turtle.getscreen()
t = turtle.Turtle()
w = Wall(s)
w.draw_wall()
r = Roof(s)
r.go_to_place()
r.draw_roof()
d = Door(s)
d.go_to_place()
d.draw_door()
t.penup()
t.goto(1000, 1000)

screen.mainloop()
