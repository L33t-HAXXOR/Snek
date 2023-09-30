from turtle import Turtle, Screen, colormode
from snek import Snek
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
colormode(255)

snek = Snek()

rng = random.randint(0, 255)

screen.listen()
screen.onkey(key="Up", fun=snek.snek_up)
screen.onkey(key="Down", fun=snek.snek_down)
screen.onkey(key="Right", fun=snek.snek_right)
screen.onkey(key="Left", fun=snek.snek_left)

game = True
while game:
    print(snek.snek[0].pos())
    if abs(snek.snek[0].xcor()) >= 260 or abs(snek.snek[0].ycor()) >= 260:
        game = False
    snek.snek_move()
    screen.update()
    time.sleep(0.1)

# Movement

screen.exitonclick()