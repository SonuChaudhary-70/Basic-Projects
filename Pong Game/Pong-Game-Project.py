# Simple Pong in Python 3 for Beginners
# By Sonu Chaudhary with the help of @TokyoEdTech

import turtle            # turtle is used to draw picture and for the windows output screen
import winsound as So    

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("sky blue")
wn.setup(width=800, height=600)
wn.tracer(15)

# Score

score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.turtlesize(stretch_wid=5, stretch_len=1)
paddle_a.color('green')
paddle_a.shape('square')
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.turtlesize(stretch_wid=5, stretch_len=1)
paddle_b.color('green')
paddle_b.shape('square')
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.color('red')
ball.shape('circle')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=("Arial", 24, 'italic'))


# Moving Paddles and Ball
# Move Paddle A upward
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    # if y > 3000:
    #     wn.onkeypress(paddle_a_up,'Stop', 'w')


# Move Paddle A downward
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

# Move Paddle B upward
def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

# Move Paddle B downward
def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

# Binding Keys of keyboard with paddles and ball to move

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, '8')
wn.onkeypress(paddle_b_down, '2')


while True:
    wn.update()

    # here we move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Set border to ball

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        So.PlaySound('bounce.wav', So.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        So.PlaySound('bounce.wav', So.SND_ASYNC)

    if ball.xcor() > 390:
        ball.setx(390)
        # ball.goto(0,0)
        ball.dx*=-1
        So.PlaySound('bounce.wav', So.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=("Arial", 24, 'italic'))


    if ball.xcor() < -390:
        ball.setx(-390)
        # ball.goto(0,0)
        ball.dx*=-1
        So.PlaySound('bounce.wav', So.SND_ASYNC)
        score_b+=1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=("Arial", 24, 'italic'))

# Set Borders to Paddles
    # if paddle_a_up.xcor > 300 :
    #     paddle_a_up.setx(390)

    #     wn.onkeypress(paddle_a_up,'Stop', 'w')
    


    # Paddle and ball collisions
    
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        So.PlaySound('game.wav', So.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        So.PlaySound('game.wav', So.SND_ASYNC)

