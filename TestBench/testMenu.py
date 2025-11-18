
import turtle
from pynput import keyboard
import threading
import time
import random

delay_Time = 0.01
DELAY = 100

game_State = False
screen = turtle.Screen()

box1 = turtle.Turtle()
player = turtle.Turtle("square")
playerdirection = "u"
player_Last_Input = 0

box1.hideturtle()
box1.color("cyan")

randx = random.randint(100, 270)
randy = random.randint(100, 270)



def drawBox(xCoord, yCoord, turt):
    turt.penup()
    turt.goto(xCoord, yCoord)  
    turt.pendown()

    for i in range(4):
        turt.forward(100)
        turt.left(90)

def INIT():
    drawBox(randx, randy, box1)

    box1.penup()

    box1.goto(randx, (randy - 50))

    box1.pendown()
    

    box1.write("start", font= ('arial', 20, 'bold'))

def on_press_menu(key):
    global playerdirection, player_Last_Input, delay_Time

    currentTime = time.time()

    try:
        if key == keyboard.Key.up:
            if currentTime - player_Last_Input > delay_Time:
                playerdirection = "u"
                player_Last_Input = currentTime
            else:
                print("Too Early on Up Key")

        elif key == keyboard.Key.right:
            if currentTime - player_Last_Input > delay_Time:
                playerdirection = "r"
                player_Last_Input = currentTime
            else:
                print("Too Early on right Key")

        elif key == keyboard.Key.left:
            if currentTime - player_Last_Input > delay_Time:
                playerdirection = "l"
                player_Last_Input = currentTime
            else:
                print("Too Early on left Key")

        elif key == keyboard.Key.down:
            if currentTime - player_Last_Input > delay_Time:
                playerdirection = "d"
                player_Last_Input = currentTime
            else:
                print("Too Early on Down Key")

    except AttributeError:
        pass

def menu_Loop():
    global randy, randx, game_State

    

    """Pynput listener. Runs on separate thread to read inputs while turtle draws"""
    pynput_listener = keyboard.Listener(on_press=on_press_menu)
    pynput_listener_thread = threading.Thread(target=pynput_listener.start)
    pynput_listener_thread.daemon = True # Allow program to exit even if this thread is running
    pynput_listener_thread.start()

    px, py = player.pos()

    if playerdirection == "u":
        py += 10    
    elif playerdirection == "r":
        px += 10
    elif playerdirection == "d":
        py -= 10
    elif playerdirection == "l":
        px -= 10

    player.goto(px, py)

    if (px > randx and px < (randx + 100)) and (py > randy and py < (randy + 100)):
        return True
    
    screen.update()
    screen.ontimer(menu_Loop, DELAY)
    
INIT()
menu_Loop()
screen.mainloop()