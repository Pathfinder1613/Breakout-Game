import turtle
from paddle import Paddle
from Ball import Ball
from Hud import HUD
from Bricks import Brick
from mainMeun import MainMenu
from powerUp import PowerUp
import time
import random

wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

game_state = "menu"
GameOver = False
ballHolding = True

moving_left = False
moving_right = False


paddle = Paddle()
ball = Ball(paddle)
Hud = HUD()
Hud.update_hud()
Main_Menu = MainMenu(0, 0)
bricks = []
powerups = []
extra_balls = []

def draw_bricks():
    bricks.clear()
    for i in range(5):
        for j in range(10):
            brick = Brick(-350 + j * 70, 250 - i * 30)
            bricks.append(brick)

def move_left():
    paddle.move_left()

def move_right():
    paddle.move_right()

def up_right():
    global ballHolding 
    if ballHolding:
        ballHolding = False
        ball.set_dx(0) 
        ball.set_dy(4)

def main_menu():
    Main_Menu.show_menu()

main_menu()

def reset_game(lives=99, score=0, rounds=1):
    global GameOver, ballHolding
    GameOver = False
    ballHolding = True
    Hud.lives = lives
    Hud.score = score
    Hud.numaberGame = rounds
    Hud.update_hud()
    ball.reset_position()
    draw_bricks()

def normal():
    global game_state
    if game_state == "menu":
        game_state = "normal"
        reset_game(lives=5, score=0, rounds=1)
    else:
        game_state = "menu"

def hard():
    global game_state
    if game_state == "menu":
        game_state = "hard"
        reset_game(lives=3, score=0, rounds=1)
    else:
        game_state = "menu"

def powergame():
    global game_state
    if game_state == "menu":
        game_state = "powergame"
        reset_game(lives=3, score=0, rounds=1)
    else:
        game_state = "menu"

def insane():
    global game_state
    if game_state == "menu":
        game_state = "insane"
        reset_game(lives=1, score=0, rounds=1)
    else:
        game_state = "menu"
    

def replay():
    global GameOver
    if GameOver:
        main_menu()

wn.listen()

wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(up_right, "Up")
wn.onkeypress(normal, "1")
wn.onkeypress(hard, "2")
wn.onkeypress(powergame, "3")
wn.onkeypress(insane, "4")
wn.onkeypress(replay, "r")

while not GameOver:
    
    
    wn.update()
    time.sleep(0.01)

    if game_state == "menu":
        paddle.hideturtle()
        ball.hideturtle()
        # Main_Menu.show_menu()
        continue
    else:
        paddle.showturtle()
        ball.showturtle()
        Main_Menu.hide_menu()

    if ballHolding:
        ball.goto(paddle.get_x(), paddle.get_y() + 20)
        continue
    
    if moving_left:
        paddle.move_left()
    if moving_right:
        paddle.move_right()
        
    ball.move()
    if ball.xcor() > 390:
        ball.setx(390)
        ball.bounce_x()
        if ball.dx == 0:
            ball.set_dx(random.choice([-2, 2]))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.bounce_x()
        if ball.dx == 0:
            ball.set_dx(random.choice([-2, 2]))

    if ball.ycor() > 290:
        ball.sety(290)
        ball.bounce_y()
        if ball.dx == 0:
            ball.set_dx(random.choice([-2, 2]))

    if ball.ycor() < -290:
        ball.sety(-290)
        ballHolding = True
        ball.reset_position()
        Hud.lose_life()
        
    if -260 < ball.ycor() < -240 and ball.dy < 0:
        if paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            ball.sety(-240)
            ball.bounce_y()

    for brick in bricks[:]:
        if brick.isvisible() and (
            brick.get_x() - 35 < ball.xcor() < brick.get_x() + 35 and
            brick.get_y() - 15 < ball.ycor() < brick.get_y() + 15
        ):
            ball.bounce_y() 
            if ball.dx == 0:
                ball.set_dx(random.choice([-2, 2]))
            x = brick.get_x()
            y = brick.get_y()
            brick.destroy()
            bricks.remove(brick)
            Hud.update_score()

            if game_state == "powergame" or game_state == "insane":
                if random.random() < 0.3:  # 30% chance
                    powerup = PowerUp(x, y)
                    powerups.append(powerup)

    for p in powerups[:]:
        p.move()
        # remove if off screen
        if p.ycor() < -300:
            p.hideturtle()
            powerups.remove(p)

        half = paddle.get_width() / 2
        
        if -260 < p.ycor() < -240 and p.dy < 0:
            if paddle.xcor() - half < p.xcor() < paddle.xcor() + half:
                p.hideturtle()
                powerups.remove(p)
                power_type = p.get_type()
                if power_type == "expand":
                    if game_state == "insane":
                        # it shriks the paddke
                        # paddle.set_size(stretch_wid=1, stretch_len=3)
                        # wn.ontimer(paddle.reset_size(), 5000)
                        print("Shrink power-up collected! (Not implemented yet)")
                    else:
                        # paddle.set_size(stretch_wid=1, stretch_len=7)
                        # wn.ontimer(paddle.reset_size(), 5000)
                        print("Expand power-up collected! (Not implemented yet)")
                
                elif power_type == "slow":
                    if not hasattr(ball, "original_speed"):
                        ball.original_speed = (ball.dx, ball.dy)
                    ball.set_dx(ball.dx * 0.5)
                    ball.set_dy(ball.dy * 0.5)

                    def reset_speed():
                        if hasattr(ball, "original_speed"):
                            dx, dy = ball.original_speed
                            ball.set_dx(dx)
                            ball.set_dy(dy)
                            del ball.original_speed

                    wn.ontimer(reset_speed, 5000)
                    
                        
                elif power_type == "multiball":
                    if game_state == "insane":
                        for _ in range(2):
                            new_ball = Ball(paddle, color="white")
                            new_ball.set_dx(random.choice([-2, 2]))
                            new_ball.set_dy(4)
                            extra_balls.append(new_ball)
                    else:
                        for _ in range(1):
                            new_ball = Ball(paddle, color=random.choice(["yellow", "cyan", "magenta"]))
                            new_ball.set_dx(random.choice([-2, 2]))
                            new_ball.set_dy(4)
                            extra_balls.append(new_ball)

                elif power_type == "speedUpPaddle":
                    if game_state == "insane":
                        paddle.set_speed(60)
                    else:
                        paddle.set_speed(40)

                    def reset_paddle_speed():
                        paddle.set_speed(20)

                    wn.ontimer(reset_paddle_speed, 5000)
                    

                
                    

    extra_balls[:] = [b for b in extra_balls if b.isvisible()]
    for b in extra_balls:
        b.move()
        if b.xcor() > 390 or b.xcor() < -390:
            b.bounce_x()
        if b.ycor() > 290:
            b.bounce_y()
        if b.ycor() < -290:
            b.hideturtle()
            extra_balls.remove(b)
        if -260 < b.ycor() < -240 and b.dy < 0:
            if paddle.xcor() - 50 < b.xcor() < paddle.xcor() + 50:
                b.sety(-240)
                b.bounce_y()
        if b.isvisible():
            for brick in bricks[:]:
                if brick.isvisible() and (
                    brick.get_x() - 35 < b.xcor() < brick.get_x() + 35 and
                    brick.get_y() - 15 < b.ycor() < brick.get_y() + 15
                ):
                    b.bounce_y()
                    if b.dx == 0:
                        b.set_dx(random.choice([-2, 2]))
                    x = brick.get_x()
                    y = brick.get_y()
                    brick.destroy()
                    bricks.remove(brick)
                    Hud.update_score()

                    if random.random() < 0.3: 
                        powerup = PowerUp(x, y)
                        powerups.append(powerup)

        

    if len(bricks) == 0:
        Hud.rounds()
        draw_bricks()
        ballHolding = True
        ball.reset_position()

    if Hud.lives <= 0:
        GameOver = True
        Hud.game_over()

wn.mainloop()