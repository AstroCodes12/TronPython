import turtle
import GameFunctions

Tron_Trail = set()
Clu_Trail = set()
TronPos = set()
CluPos = set()

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

def Tron_F():
    Tron.forward(10)
    screen.delay(DELAY)

def Clu_L():
    Clu.left(90)
    screen.delay(DELAY)

def Clu_R():
    Clu.right(90)
    screen.delay(DELAY) 

def Clu_F():
    Clu.forward(10)
    screen.delay(DELAY)

"""Record Trails and Movement Loop"""
def record_Trail():
    Tx, Ty = Tron.position()
    Tron_Trail.add((round(Tx), round(Ty)))
    Cx, Cy = Clu.position()
    Clu_Trail.add((round(Cx), round(Cy)))

    if len(Tron_Trail) > 10:
        Tron_Trail.pop() 
    if len(Clu_Trail) > 10:
        Clu_Trail.pop() 
"""
def record_Pos(TronP, CluP):
    Tx, Ty = Tron.position()
    TronP = {round(Tx, -1), round(Ty, -1)}
    Cx, Cy = Clu.position()
    CluP = {round(Cx, -1), round(Cy, -1)}
"""

def move(game_State):
    while game_State == "Alive":
        record_Trail() #Record the trails

        #Records positions
        Tx, Ty = Tron.position()
        TronPos = {round(Tx, -1), round(Ty, -1)}
        Cx, Cy = Clu.position()
        CluPos = {round(Cx, -1), round(Cy, -1)}

        #update game state based on collisions
        game_State = GameFunctions.Trail_Kill(Tron_Trail, CluPos)
        game_State = GameFunctions.Trail_Kill(Clu_Trail, TronPos)

        screen.update() #updates, reduce lag?
        print(game_State)

        #Movement Bindings
        screen.onkey(Tron_L, "a")
        screen.onkey(Tron_R, "d")
        screen.onkey(Clu_L, "Left")
        screen.onkey(Clu_R, "Right")
        screen.onkey(Tron_F, "w")
        screen.onkey(Clu_F, "Up")
        screen.listen()

    print(f"{Tron_Trail} \n\n{Clu_Trail}\n\n")
    print(f"{TronPos} \n\n{CluPos}\n\n")
    turtle.bye()
    


"""Temp Main"""
game_State_Temp = "Alive"
move(game_State_Temp)

turtle.Screen().exitonclick()