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


# Keyboard controls for the paddle
def move_left():
    x = paddle.xcor()
    if x > -240:
        x -= 20
    paddle.setx(x)


def move_right():
    x = paddle.xcor()
    if x < 240:
        x += 20
    paddle.setx(x)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    brick_row = []
    y = 200 - i * 25
    for j in range(-5, 6):
        x = j * 50
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=5)
        brick.penup()
        brick.goto(x, y)
        brick_row.append(brick)
    bricks.append(brick_row)

while True:
    screen.update()
    time.sleep(0.01)

turtle.done()
