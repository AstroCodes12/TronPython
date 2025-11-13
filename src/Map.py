import turtle
import random

screen = turtle.Screen()
border = turtle.Turtle()
grid = turtle.Turtle()


#Create Background
def create_Background():
    global screen
    screen.setup(width=750, height=750)
    screen.bgcolor("black")
    screen.setworldcoordinates(-375, -375, 375, 375)  # make (0,0) the true visual center

#Create Border
def create_Border():
    global border
    border.color("cyan")
    border.speed(0)
    border.pensize(4)
    border.penup()
    border.goto(-350, -350)
    border.pendown()

    for _ in range(4):
        border.forward(700)
        border.left(90)

    border.hideturtle()


#Create Grid Lines
def create_Grid():
    global grid
    grid.speed(0)
    grid.color("gray20")
    grid.pensize(1)

    #Vertical Lines
    for x in range(-350, 351, 25):
        grid.penup()
        grid.goto(x, -350)
        grid.pendown()
        grid.goto(x, 350)

    #Horizontal Lines
    for y in range(-350, 351, 25):
        grid.penup()
        grid.goto(-350, y)
        grid.pendown()
        grid.goto(350, y)

    grid.hideturtle()


def init_MAP():
    create_Background()
    create_Border()
    create_Grid()
