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

def plae_gaem():
    screen.resetscreen()
    snek.__init__()
    game = True
    while game:
        print(snek.snek[0].pos())
        snek.snek_move()
        screen.update()
        time.sleep(0.1)
        if abs(snek.snek[0].xcor()) >= 281 or abs(snek.snek[0].ycor()) >= 281:
            game = False


rng = random.randint(0, 255)
screen.listen()
screen.onkey(key="Up", fun=snek.snek_up)
screen.onkey(key="Down", fun=snek.snek_down)
screen.onkey(key="Right", fun=snek.snek_right)
screen.onkey(key="Left", fun=snek.snek_left)
screen.onkey(key="r", fun=plae_gaem)
screen.onkey(key="x", fun= screen.bye)


plae_gaem()


screen.exitonclick()