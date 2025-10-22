import turtle


screen = turtle.Screen()

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

def move(game_State):
    while game_State == True:
        Tron.forward(2)
        Clu.forward(2)
        screen.onkey(Tron_L, "a")
        screen.onkey(Tron_R, "d")
        screen.onkey(Clu_L, "Left")
        screen.onkey(Clu_R, "Right")
        screen.listen()
    
game_State_Temp = True
move(game_State_Temp)

turtle.Screen().exitonclick()