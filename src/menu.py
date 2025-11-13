
import turtle
import Map
import random
from pynput import keyboard
import GameFunctions
import threading
import TronEntities
import State_Controls
import time



box1 = turtle.Turtle()
player = turtle.Turtle("square")
playerdirection = "u"
player_Last_Input = 0
menuScreen = turtle.Screen()



randx = random.randint(100, 270)
randy = random.randint(100, 270)

menuStart = False

def init_Menu():
    global menuScreen
    menuScreen.setup(width=750, height=750)
    menuScreen.bgcolor("black")
    menuScreen.setworldcoordinates(-375, -375, 375, 375)  # make (0,0) the true visual center
    drawBox(randx, randy, box1)


def drawBox(xCoord, yCoord, turt):
    turt.hideturtle()
    turt.color("cyan")
    turt.penup()
    turt.goto(-100, 100)
    turt.pendown()
    turt.write("Press SPACE to start!", move=False, align='left', font=("arial", 10, "bold"))
    turt.penup()
    turt.goto(xCoord, yCoord)  
    turt.pendown()

    for i in range(4):
        turt.forward(100)
        turt.left(90)

    box1.penup()
    box1.goto(randx, (randy - 50))
    box1.pendown()
    box1.write("Start", font=('arial', 20, 'bold'))

def menu_Loop():
    global randy, randx, player_Last_Input, playerdirection, menuStart

    """Pynput listener. Runs on separate thread to read inputs while turtle draws"""
    pynput_listener = keyboard.Listener(on_press=GameFunctions.on_press)
    pynput_listener_thread = threading.Thread(target=pynput_listener.start)
    pynput_listener_thread.daemon = True # Allow program to exit even if this thread is running
    pynput_listener_thread.start()

    player.color("blue")
    px, py = player.pos()

    if menuStart:
        if playerdirection == "u":
            py += 25    
        elif playerdirection == "r":
            px += 25
        elif playerdirection == "d":
            py -= 25
        elif playerdirection == "l":
            px -= 25

        player.goto(px, py)
    else:
        while menuStart == False:
            currentTime = time.time()
            while not currentTime < currentTime + 1:
                player.hideturtle()
                
            currentTime = time.time()
            while not currentTime < currentTime + 1:
                player.showturtle()
                currentTime = time.time()
            

    if (px > randx and px < (randx + 100)) and (py > randy and py < (randy + 100)):
        TronEntities.game_State = True
        
    if not TronEntities.game_State:
        Map.screen.update()
        Map.screen.ontimer(menu_Loop, GameFunctions.DELAY)
    else:
        player.hideturtle()
        player.reset()
        menuScreen.reset()
        playerdirection = "u"
        player_Last_Input = 0
        menuStart = False
        State_Controls.runGame()
