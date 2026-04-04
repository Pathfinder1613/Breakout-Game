import turtle as t

class HUD(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-390, 260)
        self.lives = 99
        self.score = 0
        self.numaberGame = 1

    def update_hud(self):
        self.clear()
        self.write(f"[playerName] Score: {self.score}, Lives: {self.lives}, Rounds: {self.numaberGame}" , align="left", font=("Arial", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.update_hud()
    
    def lose_life(self):
        self.lives -= 1
        self.update_hud()

    def rounds(self):
        self.numaberGame += 1
        self.update_hud()

    def game_over(self):
        self.clear()
        self.hideturtle()
        self.goto(0, 0)  
        self.write(
            f"GAME OVER\n\nYour Score: {self.score}\n\nPress 'R' to Replay",
            align="center",
            font=("Arial", 24, "bold")
        )

