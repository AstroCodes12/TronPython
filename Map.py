import turtle

# Create window
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Tron Border Test")

# Create border
border = turtle.Turtle()
border.color("cyan")
border.pensize(4)
border.penup()
border.goto(-200, -200)
border.pendown()

for _ in range(4):
    border.forward(400)
    border.left(90)

border.hideturtle()

# Keep window open
turtle.done()