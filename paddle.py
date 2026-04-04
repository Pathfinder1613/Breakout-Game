import turtle as t

class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

        self.speed(0)

        self.move_speed = 20
        self.default_speed = 20
        self.set_size(1, 5)

    def move_left(self):
        x = self.xcor() - self.move_speed
        self.setx(max(x, -350))

    def move_right(self):
        x = self.xcor() + self.move_speed
        self.setx(min(x, 350))

    def reset_speed(self):
        self.move_speed = self.default_speed
    
    def set_speed(self, speed):
        self.move_speed = min(speed, 80)
        
    def get_x(self):
        return self.xcor()
    
    def get_y(self):
        return self.ycor()
    
    def set_size(self, stretch_wid, stretch_len):
        self.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
        self.width = stretch_len * 20  # keep collision accurate

    def reset_size(self):
        self.set_size(1, 5)

    def get_width(self):
        return self.width
    
    def get_x(self):
        return self.xcor()

    def get_y(self):
        return self.ycor()
    