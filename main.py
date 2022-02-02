# Simple Tennis Game for Beginners
# By @NijatMansimov

import turtle
import winsound

wn = turtle.Screen()
wn.title("Tennis by @NijatMansimov")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer()

# Score
score_a = 0
score_b = 0

# Gamer A
gamer_a = turtle.Turtle()
gamer_a.speed(0)
gamer_a.shape("square")
gamer_a.color("black")
gamer_a.shapesize(stretch_wid=5, stretch_len=1)
gamer_a.penup()
gamer_a.goto(-350, 0)

# Gamer B
gamer_b = turtle.Turtle()
gamer_b.speed(0)
gamer_b.shape("square")
gamer_b.color("black")
gamer_b.shapesize(stretch_wid=5, stretch_len=1)
gamer_b.penup()
gamer_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font="Couruer 24 normal")


# Functions
def gamer_a_up():
    y = gamer_a.ycor()
    y += 20
    gamer_a.sety(y)


def gamer_a_down():
    y = gamer_a.ycor()
    y -= 20
    gamer_a.sety(y)


def gamer_b_up():
    y = gamer_b.ycor()
    y += 20
    gamer_b.sety(y)


def gamer_b_down():
    y = gamer_b.ycor()
    y -= 20
    gamer_b.sety(y)


# Keyboard listen
wn.listen()
wn.onkeypress(gamer_a_up, "w")
wn.onkeypress(gamer_a_down, "s")
wn.onkeypress(gamer_b_up, "Up")
wn.onkeypress(gamer_b_down, "Down")

# Game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font="Couruer 24 normal")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font="Couruer 24 normal")

    # Gamer and ball collisions
    if (340 < ball.xcor() < 350) and (
            gamer_b.ycor() + 50 > ball.ycor() > gamer_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (
            gamer_a.ycor() + 50 > ball.ycor() > gamer_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)