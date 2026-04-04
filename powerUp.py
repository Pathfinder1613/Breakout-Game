import turtle
import random

class PowerUp(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(["green", "blue", "red"]))
        self.penup()
        self.goto(x, y)

        self.type = random.choice(["expand", "slow", "multiball", "speedUpPaddle"])
        self.dy = -2

    def move(self):
        self.sety(self.ycor() + self.dy)

    def get_type(self):
        return self.type
    