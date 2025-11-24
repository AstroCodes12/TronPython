import turtle

screen = turtle.Screen()

border = None
grid = None


def create_Background():
    """Makes background black and sets dimensions"""
    global screen
    screen.setup(width=750, height=750)
    screen.bgcolor("black")
    screen.setworldcoordinates(-375, -375, 375, 375)  # make (0,0) the true visual center

    # After setworldcoordinates, hide the menu pen if it exists
    import MainMenu
    if MainMenu.pen is not None:
        MainMenu.pen.hideturtle()
        MainMenu.pen.penup()


def create_Border():
    """Draws the outer border"""
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
    """Draws the background grid"""
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
    """Draws background, Borders, and Grid"""
    create_Background()
    create_Border()
    create_Grid()