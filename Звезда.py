import turtle

screen = turtle.getscreen()
t = turtle.Turtle()


# for i in range(60):
#     t.forward(180)     Просто Красиво
#     t.left(126)

# t.speed(60)
# for i in range(30):
#     t.forward(180)        ЗВЕЗДА
#     t.left(186)


class DrawShape:
    def draw(self, sides, angle):
        for distance in sides:
            t.forward(distance)
            t.left(angle)


class Rectangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90


class Triangle(DrawShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 120


class Cube(DrawShape):
    def __init__(self):
        self.sides = [100] * 4
        self.angle = 90

cube = Cube()
cube.draw(cube.sides, cube.angle)
t.forward(100)
t.left(45)
t.forward(40)
t.left(45)
t.forward(100)
t.left(135)
t.forward(40)
t.left(180)
t.forward(40)
t.left(135)
t.forward(100)
t.left(45)
t.forward(40)
screen.mainloop()
