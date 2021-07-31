import turtle
import random

sc = turtle.getscreen()
size = int(input('Размер поля: '))
linet = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
turtles = (t1, t2, t3, t4)
for q in turtles:
    q.penup()
sc.bgcolor('green')

t2.goto(0, 40)
t3.goto(0, 80)
t4.goto(0, 120)

t1.color('yellow')
t2.color('red')
t3.color('blue')

for q in turtles:
    q.pendown()

t1x = 0
t2x = 0
t3x = 0
t4x = 0

while t1x < size or t2x < size or t3x < size or t4x < size:
    for q in turtles:
        q.forward(random.uniform(0, 10))
        t1x = t1.xcor()
        t2x = t2.xcor()
        t3x = t3.xcor()
        t4x = t4.xcor()
        print(t1x)
t1x = t1.xcor()
t2x = t2.xcor()
t3x = t3.xcor()
t4x = t4.xcor()
mtx = max(t1x, t2x, t3x, t4x)
if t1x == mtx:
    print('YELLOW IS WINNER')
elif t2x == mtx:
    print('RED IS WINNER')
elif t3x == mtx:
    print('BLUE IS WINNER')
elif t4x == mtx:
    print('BLACK IS WINNER')
sc.mainloop()
