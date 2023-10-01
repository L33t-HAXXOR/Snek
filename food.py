from turtle import Turtle
from snek import Snek
import random as r

s = Snek()

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.spawn(s.snek)


    def spawn(self, deadzone):
        new_x = r.randrange(-280, 280, 20)
        new_y = r.randrange(-280, 280, 20)
        candidate = (new_x, new_y)
        if candidate not in deadzone:
            self.goto(candidate[0], candidate[1])
        else:
            self.spawn(self. deadzone)

