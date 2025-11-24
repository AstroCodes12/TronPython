import TronEntities
from pynput import keyboard
import Map
import time
import State_Controls
import ScoreMgr

<<<<<<< HEAD
"""Entities"""
Tron = TronEntities.Tron
=======
'''Entities'''
>>>>>>> 93b7c1e (Game finished!!)
Tron_Trail = TronEntities.Tron_Trail

Clu_Trail = TronEntities.Clu_Trail

<<<<<<< HEAD
<<<<<<< HEAD
"""Game Variables"""
game_State = TronEntities.game_State

=======
>>>>>>> 0ad9867 (Changed main menu to be navigate into the box to start. Menu to game and back to menu works, when configured this way)

=======
>>>>>>> 93b7c1e (Game finished!!)
"""Player Directions"""
Trondirection = "u"
CluDirection = "u"

"""Time Delay"""
Tron_Last_Input = 0
Clu_Last_Input = 0
delay_Time = 0.2  # Seconds between accepted inputs

<<<<<<< HEAD
"""Grid Movements"""
Step = 25 # pixels per step -- keep at this size to keep the players on the grid
DELAY = 100 #Miliseconds between movements (reduces lag)
=======
'''Grid Movements'''
Step = 25  # pixels per step -- keep at this size to keep the players on the grid
DELAY = 100  # Miliseconds between movements (reduces lag)
>>>>>>> 93b7c1e (Game finished!!)

"""Screen Access"""
screen = Map.screen


def killing_Animation(player):
    """Runs score logic, sends back to menu, and runs flashing animation for turtles"""
    
    global Tron_Trail, Clu_Trail
    for i in range(4):
        player.hideturtle()
        time.sleep(.5)
        player.showturtle()
        time.sleep(.5)

    # Determine winner and update score
    if player == TronEntities.Tron:
        print("Clu wins!")
        ScoreMgr.update_winner("Clu")
    elif player == TronEntities.Clu:
        print("Tron wins!")
        ScoreMgr.update_winner("Tron")

    Tron_Trail = []
    Clu_Trail = []
    TronEntities.game_State = False
    return


"""Player Direction controls"""


def Up(player):
    """Sets player Direction"""
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "d":  # Stops 180 degree turns
            print(f"Tron {Trondirection} to u")
            Trondirection = "u"
    elif player == "Clu":
        if CluDirection != "d":
            print(f"Clu {CluDirection} to u")
            CluDirection = "u"


def Down(player):
    """Sets player Direction"""
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "u":  # Stops 180 degree turns
            print(f"Tron {Trondirection} to d")
            Trondirection = "d"
    elif player == "Clu":
        if CluDirection != "u":
            print(f"Clu {CluDirection} to d")
            CluDirection = "d"


def left(player):
    """Sets player Direction"""
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "r":  # Stops 180 degree turns
            print(f"Tron {Trondirection} to l")
            Trondirection = "l"
    elif player == "Clu":
        if CluDirection != "r":
            print(f"Clu {CluDirection} to l")
            CluDirection = "l"


def right(player):
    """Sets player Direction"""
    global Trondirection
    global CluDirection
    if player == "Tron":
        if Trondirection != "l":  # Stops 180 degree turns
            print(f"Tron {Trondirection} to r")
            Trondirection = "r"
    elif player == "Clu":
        if CluDirection != "l":
            print(f"Clu {CluDirection} to r")
            CluDirection = "r"


def game_Loop():
    """This is the central game logic. This uses the keyboard readings to change player direction
        --It runs by reading player location, reading the set player direction, which may have been
        changed in the previous frame, and moving the player by 1 25 pixel step in the set direction
        --It is a recursive function and updates the screen every "Frame" 
        --It will continue to run until gamestate is changed to false, which it then runs runGame() again,
        Taking you to the menu again"""
    
    global Trondirection
    global CluDirection

    #Splits Player x and y positions
    tx, ty = TronEntities.Tron.pos()
    cx, cy = TronEntities.Clu.pos()

    record_Trail()
    TronEntities.game_State = trail_Kill()

    if Trondirection == "u":
        ty += Step #Sets going up
    elif Trondirection == "r":
        tx += Step #Sets going right
    elif Trondirection == "d":
        ty -= Step #Sets going down
    elif Trondirection == "l":
        tx -= Step #Sets going left

    if CluDirection == "u":
        cy += Step
    elif CluDirection == "r":
        cx += Step
    elif CluDirection == "d":
        cy -= Step
    elif CluDirection == "l":
        cx -= Step

    #Looks for border collision
    if tx < -350 or tx > 350 or ty > 350 or ty < -350:
        killing_Animation(TronEntities.Tron)

    if cx < -350 or cx > 350 or cy > 350 or cy < -350:
        killing_Animation(TronEntities.Clu)

    #Moves players
    TronEntities.Tron.goto(tx, ty)
    TronEntities.Clu.goto(cx, cy)

    #Checks game state
    if TronEntities.game_State == True:
        screen.update()  # Must run at bottom of function, before .ontimer, which calls the function again
        screen.ontimer(game_Loop, DELAY)  # Calls the function again, causing a loop. DELAY is to reduce glitches
    else:
        print(f" game state: {TronEntities.game_State}")
        screen.clear()
        Trondirection = "u"
        CluDirection = "u"
        State_Controls.runGame()


"""Keyboard Recording"""
def on_press(key):
    """This uses Pynput's keyboard method to read for inputs from the keyboard. I used this instead of turtle's input readings
        so that I could run the listener and game logic on separate threads, increasing efficiency"""
    
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
            if TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    Up("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on Up Key")

        elif key == keyboard.Key.right:

            if TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    right("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on right Key")

        elif key == keyboard.Key.left:

            if TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    left("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on left Key")

        elif key == keyboard.Key.down:

            if TronEntities.game_State:
                if currentTime - Clu_Last_Input > delay_Time:
                    Down("Clu")
                    Clu_Last_Input = currentTime
            else:
                print("Too Early on Down Key")

    except AttributeError:
        pass

"""Record Trails and Movement Loop"""


def record_Trail():
    """Records every previous position of the players"""
    Tron_Trail.append(TronEntities.Tron.pos())  # Appends new values to lists
    Clu_Trail.append(TronEntities.Clu.pos())


def trail_Kill():
    """Looks for each players current position in the opposing player's previous positions list as well as it's own list
        --If it finds the current position in the list, it sets game state to false, ending the game"""
    
    global Tron_Trail
    global Clu_Trail

    Tron_set = set(Tron_Trail)
    Clu_set = set(Clu_Trail)

    same = Tron_set & Clu_set

    if len(same) != 0:
        #Checks for who won
        if TronEntities.Tron.pos() in same and not TronEntities.Clu.pos() in same:
            killing_Animation(TronEntities.Tron)
        
        if TronEntities.Clu.pos() in same and not TronEntities.Tron.pos() in same:
            killing_Animation(TronEntities.Clu)

        if TronEntities.Clu.pos() in same and TronEntities.Tron.pos() in same:
            for i in range(4):
                TronEntities.Tron.hideturtle()
                TronEntities.Clu.hideturtle()
                time.sleep(0.5)
                TronEntities.Tron.showturtle()
                TronEntities.Clu.showturtle()
                time.sleep(0.5)
        else:
            print("No player collisions or backtracks detected")

        #Resets all lists for next round
        same.clear()
        Tron_set.clear()
        Clu_set.clear()
        Tron_Trail = []
        Clu_Trail = []
        Clu_Trail = []
        return False

    elif len(Tron_Trail) != len(Tron_set):
        killing_Animation(TronEntities.Tron)
        
        same.clear()
        Tron_set.clear()
        Clu_set.clear()
        Tron_Trail = []
        Clu_Trail = []
        return False
    
    elif len(Clu_Trail) != len(Clu_set):
        killing_Animation(TronEntities.Clu)

        same.clear()
        Tron_set.clear()
        Clu_set.clear()
        Tron_Trail = []
        Clu_Trail = []
        return False
    
    else:
        return True
