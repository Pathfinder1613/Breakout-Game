import turtle as t 

class MainMenu(t.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)

    def draw_menu(self):
        self.clear()
        self.goto(0, 100)
        self.write("BREAKOUT", align="center", font=("Arial", 28, "bold"))

        self.goto(0, 0)
        self.write(
            "1: Normal\n2: Hard\n3: Power Up Game \n4: Insane Mode",
            align="center",
            font=("Arial", 18, "normal")
        )

    def show_menu(self):
        self.draw_menu()
    
    def hide_menu(self):
        self.clear()