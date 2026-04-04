import turtle as t

class Brick(t.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("white")
        self.penup()
        self.goto(x, y)
    
    def get_x(self):
        return self.xcor()
    def get_y(self):
        return self.ycor()
    def destroy(self):
        self.hideturtle()
        self.goto(1000, 1000) 

 
    
