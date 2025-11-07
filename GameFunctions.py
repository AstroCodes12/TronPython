import turtle
import TronEntities
from pynput import keyboard
import math
import Map


'''Entities'''
Tron = TronEntities.Tron
Clu = TronEntities.Clu
game_State = True

'''Grid Movements'''
Step = 25       # pixels per step
DELAY = 10
PROX_THRESHOLD = 10

'''Screen Access'''
screen = Map.screen

def game_Loop(gameState=game_State):
    global w_State
    global d_State
    global a_State
    global s_State

    global up_State
    global right_State
    global left_State
    global down_State
    
    global Trondirection
    global CluDirection

    tx, ty = Tron.pos()
    cx, cy = Tron.pos()

    while game_State:
        record_Trail()
        if w_State:
            if Trondirection != "d": #Stops 180 degree turns
                Trondirection = "u"
                ty += Step    
        elif d_State:
            Trondirection = "r"
            tx += Step
        elif s_State:
            if Trondirection != "u": #Stops 180 degree turns
                Trondirection = "d"
                ty -= Step
        elif a_State:
            Trondirection = "l"
            tx -= Step

        elif up_State:
            if CluDirection != "d": #Stops 180 degree turns
                CluDirection = "u"
                cy += Step
        elif right_State:
            CluDirection = "r"
            cx += Step
        elif left_State:
            CluDirection = "l"
            cx -= Step
        elif down_State:
            if CluDirection != "u": #Stops 180 degree turns
                CluDirection = "d"
                cy -= Step

        Tron.goto(tx, ty)
        Clu.goto(cx, cy) 

        compare_Pos()
        screen.update()



"""Keyboard States"""
w_State = False
a_State = False
d_State = False
s_State = False

up_State = False
right_State = False
left_State = False
down_State = False

Trondirection = "u"
CluDirection = "u"

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
    global s_State

    global up_State
    global right_State
    global left_State
    global down_State

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
        elif key == keyboard.KeyCode.from_char("s"):
            s_State = True
        elif key == keyboard.Key.up:
            up_State = True
            #print("up key pressed - up_State set to True")
        elif key == keyboard.Key.right:
            right_State = True
            #print("right key pressed - right_State set to True")
        elif key == keyboard.Key.left:
            left_State = True
            #print("left key pressed - left_State set to True")
        elif key == keyboard.Key.down:
            down_State = True
    except AttributeError:
        pass

def on_release(key):
    global w_State
    global d_State
    global a_State
    global s_State

    global up_State
    global right_State
    global left_State
    global down_State

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
        elif key == keyboard.KeyCode.from_char("s"):
            s_State = True
        elif key == keyboard.Key.up:
            up_State = False
            #print("up key released - up_State set to False")
        elif key == keyboard.Key.right:
            right_State = False
            #print("right key released - right_State set to False")
        elif key == keyboard.Key.left:
            left_State = False
            #print("left key released - left_State set to False")
        elif key == keyboard.Key.down:
            down_State = True

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
