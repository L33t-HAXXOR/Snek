from turtle import Turtle, write
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Bord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.hideturtle()
        self.peepin_pointz()


    def peepin_pointz(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def u_ded(self):
        self.goto(0, 0)
        self.color("red")
        self.write("U ded", font=("Arial", 50, "normal"), align=ALIGNMENT)


    def moar_pointz(self):
        self.score += 1
        self.clear()
        self.peepin_pointz()