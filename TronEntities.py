import turtle
import TrailFunction
import GameFunctions

Tron_Trail = []
Clu_Trail = []

screen = turtle.Screen()

"""Entity INIT"""
Tron = turtle.Turtle("arrow")
Tron.color("blue")
Tron.penup()
Tron.goto(-200, 0)
Tron.pendown()
Tron.setheading(0)

Clu = turtle.Turtle("arrow")
Clu.color("red")
Clu.penup()
Clu.goto(200, 0)
Clu.pendown()
Clu.setheading(180)

SPEED = 2        # pixels per step
DELAY = 10       # milliseconds between steps

"""Movement Functions
"""
def Tron_L():
    Tron.left(90)
    screen.delay(DELAY)
    
def Tron_R():
    Tron.right(90)
    screen.delay(DELAY)

def Clu_L():
    Clu.left(90)
    screen.delay(DELAY)

def Clu_R():
    Clu.right(90)
    screen.delay(DELAY) 

"""Record Trails and Movement Loop"""
def record_trail():
    Tron_Trail.append(Tron.position())
    Clu_Trail.append(Clu.position())
    if len(Tron_Trail) > 10:
        Tron_Trail.pop(0)
    if len(Clu_Trail) > 10:
        Clu_Trail.pop(0)

def move(game_State):
    while game_State == "Alive":
        Tron.forward(2)
        Clu.forward(2)
        record_trail() #Record the trails
        game_State = GameFunctions.Trail_Kill(Tron_Trail, Clu.position())
        game_State = GameFunctions.Trail_Kill(Clu_Trail, Tron.position())
        screen.update() #updates, reduce lag?
        print(game_State)
        screen.onkey(Tron_L, "a")
        screen.onkey(Tron_R, "d")
        screen.onkey(Clu_L, "Left")
        screen.onkey(Clu_R, "Right")
        screen.listen()
    


"""Temp Main"""
game_State_Temp = "Alive"
move(game_State_Temp)

turtle.Screen().exitonclick()