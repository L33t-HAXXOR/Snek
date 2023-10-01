from turtle import Turtle

class Bord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score {self.score}")
        # self.goto(0, 280)

    def u_ded(self):
        self.hideturtle()
        self.write(font=("Arial", 8, "normal"))
        self.goto(0, 0)
        self.write("U Ded")
        self.showturtle()