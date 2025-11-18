import turtle
import Map

# Entities start as placeholders; created only when the game starts
Tron = None
Clu = None

# Trails (canonical lists)
Tron_Trail = []
Clu_Trail = []

# Shared screen and game state
screen = Map.screen
game_State = True  # True == game running; controllers will set to False to stop

def Tron_INIT():
    """
    Create and initialize the Tron turtle at game start.
    """
    global Tron, Tron_Trail, game_State
    Tron_Trail = []
    game_State = True

    Tron = turtle.Turtle("square")
    Tron.hideturtle()
    Tron.color("blue")
    Tron.pensize(10)
    Tron.penup()                # important: don't draw while placing
    Tron.goto(-200, 0)
    Tron.setheading(0)
    Tron.pendown()
    Tron.showturtle()

def Clu_INIT():
    """
    Create and initialize the Clu turtle at game start.
    """
    global Clu, Clu_Trail, game_State
    Clu_Trail = []
    game_State = True

    Clu = turtle.Turtle("square")
    Clu.hideturtle()
    Clu.color("red")
    Clu.pensize(10)
    Clu.penup()                 # important: don't draw while placing
    Clu.goto(200, 0)
    Clu.setheading(180)
    Clu.pendown()
    Clu.showturtle()