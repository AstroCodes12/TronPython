import TronEntities
from pynput import keyboard
import math
import Map
import time
import menu
import State_Controls


"""Entities"""
Tron = TronEntities.Tron
Tron_Trail = TronEntities.Tron_Trail

Clu = TronEntities.Clu
Clu_Trail = TronEntities.Clu_Trail

<<<<<<< HEAD
"""Game Variables"""
game_State = TronEntities.game_State

=======
>>>>>>> 0ad9867 (Changed main menu to be navigate into the box to start. Menu to game and back to menu works, when configured this way)

"""Player Directions"""
Trondirection = "u"
CluDirection = "u"

"""Time Delay"""
Tron_Last_Input = 0
Clu_Last_Input = 0
delay_Time = 0.2 #Seconds between accepted inputs


"""Grid Movements"""
Step = 25 # pixels per step -- keep at this size to keep the players on the grid
DELAY = 100 #Miliseconds between movements (reduces lag)

"""Screen Access"""
screen = Map.screen

def killing_Animation(player):
    global Tron_Trail, Clu_Trail
    for i in range(4):
            player.hideturtle()
            time.sleep(.5)
            player.showturtle()
            time.sleep(.5)
    Tron_Trail = []
    Clu_Trail = []
    TronEntities.game_State = False



"""Direction controls"""
def Up(player):
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "d": #Stops 180 degree turns
                print(f"Tron {Trondirection} to u")
                Trondirection = "u"
    elif player == "Clu":
        if CluDirection != "d":
            print(f"Clu {CluDirection} to u")
            CluDirection = "u"

def Down(player):
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "u": #Stops 180 degree turns
                print(f"Tron {Trondirection} to d")
                Trondirection = "d"
    elif player == "Clu":
        if CluDirection != "u":
            print(f"Clu {CluDirection} to d")
            CluDirection = "d"

def left(player):
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "r": #Stops 180 degree turns
                print(f"Tron {Trondirection} to l")
                Trondirection = "l"
    elif player == "Clu":
        if CluDirection != "r":
            print(f"Clu {CluDirection} to l")
            CluDirection = "l"

def right(player):
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "l": #Stops 180 degree turns
                print(f"Tron {Trondirection} to r")
                Trondirection = "r"
    elif player == "Clu":
        if CluDirection != "l":
            print(f"Clu {CluDirection} to r")
            CluDirection = "r"



def game_Loop():
    global Trondirection
    global CluDirection

    tx, ty = Tron.pos()
    cx, cy = Clu.pos()
    
    record_Trail()
    TronEntities.game_State = trail_Kill()
    
    if Trondirection == "u":
        ty += Step    
    elif Trondirection == "r":
        tx += Step
    elif Trondirection == "d":
        ty -= Step
    elif Trondirection == "l":
        tx -= Step
    
    if CluDirection == "u":
        cy += Step    
    elif CluDirection == "r":
        cx += Step
    elif CluDirection == "d":
        cy -= Step
    elif CluDirection == "l":
        cx -= Step

    if tx < -350 or tx > 350 or ty > 350 or ty < -350:
        killing_Animation(Tron)
    
    if cx < -350 or cx > 350 or cy > 350 or cy < -350:
        killing_Animation(Clu)

    Tron.goto(tx, ty)
    Clu.goto(cx, cy) 

    if TronEntities.game_State == True:
        screen.update() #Must run at bottom of function, before .ontimer, which calls the function again
        screen.ontimer(game_Loop, DELAY) #Calls the function again, causing a loop. DELAY is to reduce glitches
    else:
        print(f" game state: {TronEntities.game_State}")
        screen.reset()
        Trondirection = "u"
        CluDirection = "u"
        State_Controls.runGame()



"""Keyboard Recording"""
def on_press(key):
    global Trondirection
    global CluDirection
    global Tron_Last_Input
    global Clu_Last_Input
    
    currentTime = time.time()

    try:
        if key == keyboard.KeyCode.from_char('w'):
            if currentTime - Tron_Last_Input > delay_Time:
                Up("Tron")
                Tron_Last_Input = currentTime
            else:
                print("Too Early on u")

        elif key == keyboard.KeyCode.from_char('d'):
            if currentTime - Tron_Last_Input > delay_Time:
                right("Tron")
                Tron_Last_Input = currentTime
            else:
                print("Too Early on r")

        elif key == keyboard.KeyCode.from_char('a'):
            if currentTime - Tron_Last_Input > delay_Time:
                left("Tron")
                Tron_Last_Input = currentTime
            else:
                print("Too Early on a")

        elif key == keyboard.KeyCode.from_char("s"):
            if currentTime - Tron_Last_Input > delay_Time:
                Down("Tron")
                Tron_Last_Input = currentTime
            else:
                print("Too Early on s")
    
        elif key == keyboard.Key.up:
            if not TronEntities.game_State:
                    if menu.playerdirection != "d":
                        menu.playerdirection = "u"

            elif TronEntities.game_State:        
                if currentTime - Clu_Last_Input > delay_Time:
                    Up("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on Up Key")

        elif key == keyboard.Key.right:
            if not TronEntities.game_State:
                if menu.playerdirection != "l":
                    menu.playerdirection = 'r'

            elif TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    right("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on right Key")

        elif key == keyboard.Key.left:
            if not TronEntities.game_State:
                if menu.playerdirection != "r":
                    menu.playerdirection = 'l'

            elif TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    left("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on left Key")

        elif key == keyboard.Key.down:
            if not TronEntities.game_State:
                if menu.playerdirection != "u":
                    menu.playerdirection = "d"

            elif TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    Down("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on Down Key")
        elif key == keyboard.Key.space:
            if TronEntities.game_State == False:
                menu.menuStart = True

    except AttributeError:
        pass

""" Keeping just in case. Use to run things on the release of a key!
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
            s_State = False
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
            down_State = False

    except AttributeError:
        pass    
"""
"""Record Trails and Movement Loop"""
def record_Trail():
    Tron_Trail.append(Tron.pos()) #Appends new values to lists
    Clu_Trail.append(Clu.pos())

    

def trail_Kill():
    global Tron_Trail
    global Clu_Trail

    Tron_set = set(Tron_Trail)
    Clu_set = set(Clu_Trail)

    same = Tron_set & Clu_set

    if len(same) != 0:
        for i in range(4):
            Tron.hideturtle()
            Clu.hideturtle()
            time.sleep(.5)
            Tron.showturtle()
            Clu.showturtle()
            time.sleep(.5)

        same.clear()
        Tron_set.clear()
        Clu_set.clear()
        Tron_Trail = []
        Clu_Trail = []
        print("collision")
        return False

    elif len(Tron_Trail) != len(Tron_set) or len(Clu_Trail) != len(Clu_set):
        for i in range(4):
            Tron.hideturtle()
            Clu.hideturtle()
            time.sleep(.5)
            Tron.showturtle()
            Clu.showturtle()
            time.sleep(.5)

        same.clear()
        Tron_set.clear()
        Clu_set.clear()
        Tron_Trail = []
        Clu_Trail = []
        print("Backtrack")
        return False
    else:
        return True
