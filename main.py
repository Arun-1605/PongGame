from turtle import Screen
from Paddle import Paddle
from ball import Ball
import time
from score import Score




screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball =Ball()
score  =Score()



screen.listen()
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")


is_gameOn = True

while is_gameOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    # if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        

screen.exitonclick()