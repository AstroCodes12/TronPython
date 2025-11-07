import turtle
import GameFunctions
from pynput import keyboard
import threading
import math


Tron_x = []
Tron_y = []

Clu_x = []
Clu_y = []

screen = turtle.Screen() # Screen Init
game_State = True 

"""Entity INIT"""
Tron = turtle.Turtle("arrow")
Tron.color("blue")
Tron.pensize(10)
Tron.penup()
Tron.goto(-200, 0)
Tron.pendown()
Tron.setheading(0)

Clu = turtle.Turtle("arrow")
Clu.color("red")
Clu.pensize(10)
Clu.penup()
Clu.goto(200, 0)
Clu.pendown()
Clu.setheading(180)

SPEED = 10        # pixels per step
DELAY = 10
PROX_THRESHOLD = 10 #Distance allowed between players

"""Keyboard States"""
w_State = False
a_State = False
d_State = False

up_State = False
right_State = False
left_State = False


"""Turn Cooldown
Tron_last_Turn = 0
Clu_Last_Turn = 0
coolDown = .75
"""

"""Keyboard Recording"""
def on_press(key):
    global w_State
    global a_State
    global d_State

    global up_State
    global right_State
    global left_State

    global game_State
    
    global Tron_last_Turn
    global Clu_Last_Turn

    try:
        if key == keyboard.KeyCode.from_char('w'):
            w_State = True
            #print("W key pressed - w_State set to True")
        elif key == keyboard.KeyCode.from_char('d'):
            d_State = True
            #print("D key pressed - d_State set to True")
        elif key == keyboard.KeyCode.from_char('a'):
            a_State = True
            #print("A key pressed - a_State set to True")
        elif key == keyboard.Key.up:
            up_State = True
            #print("up key pressed - up_State set to True")
        elif key == keyboard.Key.right:
            right_State = True
            #print("right key pressed - right_State set to True")
        elif key == keyboard.Key.left:
            left_State = True
            #print("left key pressed - left_State set to True")
    except AttributeError:
        pass

def on_release(key):
    global w_State
    global d_State
    global a_State

    global up_State
    global right_State
    global left_State

    global game_State

    global Tron_last_Turn
    global Clu_Last_Turn
    try:
        if key == keyboard.KeyCode.from_char('w'):
            w_State = False
            #print("W key released - w_State set to False")
        elif key == keyboard.KeyCode.from_char('d'):
            d_State = False
            #print("D key released - d_State set to False")
        elif key == keyboard.KeyCode.from_char('a'):
            a_State = False
            #print("A key released - a_State set to False")
        elif key == keyboard.Key.up:
            up_State = False
            #print("up key released - up_State set to False")
        elif key == keyboard.Key.right:
            right_State = False
            #print("right key released - right_State set to False")
        elif key == keyboard.Key.left:
            left_State = False
            #print("left key released - left_State set to False")

    except AttributeError:
        pass    

"""Record Trails and Movement Loop"""
def record_Trail():
    tx, ty = Tron.pos() #Splits .pos() Vect2D into 2 floats
    cx, cy = Clu.pos() #^^


    Tron_x.append(tx) #Appends new values to lists
    Tron_y.append(ty)

    Clu_x.append(cx)
    Clu_y.append(cy)

    if len(Tron_x) > 100: #Pops any positions after 100 recordings
        Tron_x.pop()
    if len(Tron_y) > 100:
        Tron_y.pop()
    if len(Clu_x) > 100:
        Clu_x.pop()
    if len(Clu_y) > 100:
        Clu_y.pop() 

def distance(p1x, p2x, p1y, p2y):
    return math.sqrt((p1x - p2x)**2 + (p1y - p2y)**2)

def compare_Pos():
    global game_State
    global Tron_x
    global Tron_y
    global Clu_x
    global Clu_y

    tx, ty = Tron.pos()
    cx, cy = Clu.pos()

"""
    for step, i in enumerate(Tron_x):
        if distance(tx, Clu_x[step], ty, Clu_y[step]) < 100:
            game_State = False
            print("Collision")
    for step, i in enumerate(Clu_x):
        if distance(cx, Tron_x[step], cy, Tron_y[step]) < 100:
            game_State = False
            print("Collision")
            """

def game_Loop(gameState=game_State):
    global w_State
    global d_State
    global a_State

    while game_State:
        record_Trail()
        if w_State:
            Tron.forward(5)
        elif a_State:
            Tron.left(90)
        elif d_State:
            Tron.right(90)
        elif up_State:
            Clu.forward(5)
        elif right_State:
            Clu.right(90)
        elif left_State:
            Clu.left(90)
        compare_Pos()
        screen.update()



if game_State:
    pynput_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    pynput_listener_thread = threading.Thread(target=pynput_listener.start)
    pynput_listener_thread.daemon = True # Allow program to exit even if this thread is running
    pynput_listener_thread.start()


    game_Loop()  # Start the game loop
else:
    print("Game Over") 