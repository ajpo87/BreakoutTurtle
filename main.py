import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 3
ball.dy = -3

turtle.done()
