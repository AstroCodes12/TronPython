import TronEntities
from pynput import keyboard
import Map
import time

# Directions
Trondirection = "u"
CluDirection = "u"

# Input debounce timers
Tron_Last_Input = 0
Clu_Last_Input = 0
delay_Time = 0.2  # seconds between accepted inputs

# Movement and timing
Step = 25  # grid step
DELAY = 100  # ms between movements

# Screen reference (Map.screen is created at import)
screen = Map.screen

def killing_Animation(player):
    """Blink the losing player and set the shared game state to False."""
    for _ in range(4):
        player.hideturtle()
        time.sleep(.5)
        player.showturtle()
        time.sleep(.5)
    TronEntities.game_State = False

# Direction setters
def Up(player):
    global Trondirection, CluDirection
    if player == "Tron":
        if Trondirection != "d":
            Trondirection = "u"
    elif player == "Clu":
        if CluDirection != "d":
            CluDirection = "u"

def Down(player):
    global Trondirection, CluDirection
    if player == "Tron":
        if Trondirection != "u":
            Trondirection = "d"
    elif player == "Clu":
        if CluDirection != "u":
            CluDirection = "d"

def left(player):
    global Trondirection, CluDirection
    if player == "Tron":
        if Trondirection != "r":
            Trondirection = "l"
    elif player == "Clu":
        if CluDirection != "r":
            CluDirection = "l"

def right(player):
    global Trondirection, CluDirection
    if player == "Tron":
        if Trondirection != "l":
            Trondirection = "r"
    elif player == "Clu":
        if CluDirection != "l":
            CluDirection = "r"

def record_Trail():
    """Append current positions to the canonical trail lists."""
    if TronEntities.Tron is None or TronEntities.Clu is None:
        return
    TronEntities.Tron_Trail.append(TronEntities.Tron.pos())
    TronEntities.Clu_Trail.append(TronEntities.Clu.pos())

def trail_Kill():
    """Collision detection using the canonical trail lists in TronEntities."""
    if TronEntities.Tron is None or TronEntities.Clu is None:
        return

    Tron_set = set(TronEntities.Tron_Trail)
    Clu_set = set(TronEntities.Clu_Trail)

    if Tron_set & Clu_set:
        for _ in range(4):
            TronEntities.Tron.hideturtle()
            TronEntities.Clu.hideturtle()
            time.sleep(.5)
            TronEntities.Tron.showturtle()
            TronEntities.Clu.showturtle()
            time.sleep(.5)
        TronEntities.game_State = False
        return

    if len(TronEntities.Tron_Trail) != len(Tron_set) or len(TronEntities.Clu_Trail) != len(Clu_set):
        for _ in range(4):
            TronEntities.Tron.hideturtle()
            TronEntities.Clu.hideturtle()
            time.sleep(.5)
            TronEntities.Tron.showturtle()
            TronEntities.Clu.showturtle()
            time.sleep(.5)
        TronEntities.game_State = False
        return

def game_Loop():
    """Main loop: move both players, append trails, check collisions."""
    global Trondirection, CluDirection

    # Ensure players exist
    if TronEntities.Tron is None or TronEntities.Clu is None:
        return

    # If the shared flag is False, stop scheduling further loops
    if TronEntities.game_State is False:
        return

    tx, ty = TronEntities.Tron.pos()
    cx, cy = TronEntities.Clu.pos()

    record_Trail()
    trail_Kill()

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
        killing_Animation(TronEntities.Tron)
        return

    if cx < -350 or cx > 350 or cy > 350 or cy < -350:
        killing_Animation(TronEntities.Clu)
        return

    TronEntities.Tron.goto(tx, ty)
    TronEntities.Clu.goto(cx, cy)

    screen.update()
    screen.ontimer(game_Loop, DELAY)

def on_press(key):
    """Keyboard handler using pynput — only updates direction state (no turtle calls)."""
    global Tron_Last_Input, Clu_Last_Input
    currentTime = time.time()

    try:
        if key == keyboard.KeyCode.from_char('w'):
            if currentTime - Tron_Last_Input > delay_Time:
                Up("Tron")
                Tron_Last_Input = currentTime
        elif key == keyboard.KeyCode.from_char('d'):
            if currentTime - Tron_Last_Input > delay_Time:
                right("Tron")
                Tron_Last_Input = currentTime
        elif key == keyboard.KeyCode.from_char('a'):
            if currentTime - Tron_Last_Input > delay_Time:
                left("Tron")
                Tron_Last_Input = currentTime
        elif key == keyboard.KeyCode.from_char("s"):
            if currentTime - Tron_Last_Input > delay_Time:
                Down("Tron")
                Tron_Last_Input = currentTime

        elif key == keyboard.Key.up:
            if currentTime - Clu_Last_Input > delay_Time:
                Up("Clu")
                Clu_Last_Input = currentTime
        elif key == keyboard.Key.right:
            if currentTime - Clu_Last_Input > delay_Time:
                right("Clu")
                Clu_Last_Input = currentTime
        elif key == keyboard.Key.left:
            if currentTime - Clu_Last_Input > delay_Time:
                left("Clu")
                Clu_Last_Input = currentTime
        elif key == keyboard.Key.down:
            if currentTime - Clu_Last_Input > delay_Time:
                Down("Clu")
                Clu_Last_Input = currentTime
    except AttributeError:
        pass