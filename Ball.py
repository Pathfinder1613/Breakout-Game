import turtle as t

class Ball(t.Turtle):
    def __init__(self, paddle, color="white"):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()

        self.paddle = paddle

        self.dx = 0
        self.dy = 0

        self.goto(self.paddle.get_x(), self.paddle.get_y() + 20)

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
    
    def bounce_x(self):
        self.dx *= -1
    
    def bounce_y(self):
        self.dy *= -1
    
    def reset_position(self):
        self.goto(self.paddle.get_x(), self.paddle.get_y() + 20)
        self.dx = 0
        self.dy = 0
    
    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy