from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snek:

    def __init__(self):
        self.snek = []
        self.maek_snek()
        self.hed = self.snek[0]

    def maek_snek(self):
        for pos in START_POS:
            tort = Turtle(shape="square")
            tort.color("white")
            tort.up()
            tort.goto(pos)
            self.snek.append(tort)

    def snek_move(self):
        for seg_num in reversed(range(len(self.snek))):
            if seg_num > 0:
                self.snek[seg_num].goto(self.snek[seg_num - 1].pos())
        self.hed.fd(MOVE_DIST)

    def snek_right(self):
        if self.hed.heading() != LEFT:
            self.hed.seth(RIGHT)

    def snek_left(self):
        if self.hed.heading() != RIGHT:
            self.hed.seth(LEFT)

    def snek_up(self):
        if self.hed.heading() != DOWN:
            self.hed.seth(UP)

    def snek_down(self):
        if self.hed.heading() != UP:
            self.hed.seth(DOWN)