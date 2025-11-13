import turtle
import random

screen = turtle.Screen()
border = turtle.Turtle()
grid = turtle.Turtle()

<<<<<<< HEAD
# Create Background
=======

#Create Background
>>>>>>> 0ad9867 (Changed main menu to be navigate into the box to start. Menu to game and back to menu works, when configured this way)
def create_Background():
    """Builds the turtle screen on which the rest of the background features will be drawn"""
    global screen
    screen.setup(width=750, height=750)
    screen.bgcolor("black")
    screen.setworldcoordinates(-375, -375, 375, 375)  # Make (0,0) the true visual center

# Create Border
def create_Border():
    """Draws the border of the playable area just off the edges of the screen's width and height"""
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


# Create Grid Lines
def create_Grid():
    """Builds the grid lines across the playable area to create a 28x28 square map where each unit is 25x25 pixels"""
    global grid
    grid.speed(0)
    grid.color("gray20")
    grid.pensize(1)

    # Vertical Lines
    for x in range(-350, 351, 25):
        grid.penup()
        grid.goto(x, -350)
        grid.pendown()
        grid.goto(x, 350)

    # Horizontal Lines
    for y in range(-350, 351, 25):
        grid.penup()
        grid.goto(-350, y)
        grid.pendown()
        grid.goto(350, y)

    grid.hideturtle()


def init_MAP():
    """Calls to the previous map generation functions and puts them all into one to later be called in the main program"""
    create_Background()
    create_Border()
    create_Grid()
