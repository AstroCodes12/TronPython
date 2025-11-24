import turtle

screen = turtle.Screen()

border = None
grid = None

<<<<<<< HEAD
<<<<<<< HEAD
# Create Background
=======

<<<<<<< HEAD
#Create Background
>>>>>>> 0ad9867 (Changed main menu to be navigate into the box to start. Menu to game and back to menu works, when configured this way)
=======
# Create Background
>>>>>>> 93b7c1e (Game finished!!)
def create_Background():
    """Builds the turtle screen on which the rest of the background features will be drawn"""
=======

def create_Background():
    """Makes background black and sets dimensions"""
>>>>>>> dfdac89 (Added scoring functionality to collision function. Also added quit button and reorder menu screen. Organized and commented code)
    global screen
    screen.setup(width=750, height=750)
    screen.bgcolor("black")
    screen.setworldcoordinates(-375, -375, 375, 375)  # Make (0,0) the true visual center

<<<<<<< HEAD
=======
    # After setworldcoordinates, hide the menu pen if it exists
    import MainMenu
    if MainMenu.pen is not None:
        MainMenu.pen.hideturtle()
        MainMenu.pen.penup()


<<<<<<< HEAD
>>>>>>> 93b7c1e (Game finished!!)
# Create Border
def create_Border():
    """Draws the border of the playable area just off the edges of the screen's width and height"""
=======
def create_Border():
    """Draws the outer border"""
>>>>>>> dfdac89 (Added scoring functionality to collision function. Also added quit button and reorder menu screen. Organized and commented code)
    global border
    if border is not None:
        border.clear()  # clear any old drawings
        border.hideturtle()  # make sure it's hidden

    border = turtle.Turtle()
    border.hideturtle()
    border.color("cyan")
    border.speed(0)
    border.pensize(4)
    border.penup()
    border.goto(-350, -350)
    border.pendown()

    for _ in range(4):
        border.forward(700)
        border.left(90)
    border.penup()
    border.goto(1000, 1000)
    border.hideturtle()


# Create Grid Lines
def create_Grid():
<<<<<<< HEAD
    """Builds the grid lines across the playable area to create a 28x28 square map where each unit is 25x25 pixels"""
=======
    """Draws the background grid"""
>>>>>>> dfdac89 (Added scoring functionality to collision function. Also added quit button and reorder menu screen. Organized and commented code)
    global grid
    grid = turtle.Turtle()
    grid.hideturtle()
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
    grid.penup()
    grid.goto(1000, 1000)
    grid.hideturtle()


def init_MAP():
<<<<<<< HEAD
    """Calls to the previous map generation functions and puts them all into one to later be called in the main program"""
=======
    """Draws background, Borders, and Grid"""
>>>>>>> dfdac89 (Added scoring functionality to collision function. Also added quit button and reorder menu screen. Organized and commented code)
    create_Background()
    create_Border()
    create_Grid()