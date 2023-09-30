from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class Snek:

    def __init__(self):
        self.snek = []
        self.maek_snek()

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
        self.snek[0].fd(MOVE_DIST)

    def snek_right(self):
        self.snek[0].seth(0)

    def snek_left(self):
        self.snek[0].seth(180)

    def snek_up(self):
        self.snek[0].seth(90)

    def snek_down(self):
        self.snek[0].seth(270)