from turtle import Turtle, write

class Bord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def u_ded(self):
        self.hideturtle()
        self.write(font=("Arial", 8, "normal"))
        self.goto(0, 0)
        self.write("U Ded")
        self.showturtle()

    def moar_pointz(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))