import TronEntities
import Map
from pynput import keyboard
import GameFunctions
import threading
import turtle

# Use the shared screen from Map
screen = Map.screen

# Configure screen for menu (size etc.)
screen.setup(width=800, height=600)
screen.title("TRON game")
screen.bgcolor("black")
screen.tracer(0)

# Menu pen (only used for menu text)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pencolor("cyan")

current_option = 0  # 0 = Single Player, 1 = Two Players

def runGame():
    # Start the game only if the shared flag indicates the game is on
    if TronEntities.game_State:
        # hide/clear the menu pen so it doesn't overlap the map or confuse players
        pen.clear()
        pen.hideturtle()

        # Start pynput listener (changes only direction globals)
        pynput_listener = keyboard.Listener(on_press=GameFunctions.on_press)
        pynput_thread = threading.Thread(target=pynput_listener.start)
        pynput_thread.daemon = True
        pynput_thread.start()

        # Draw map and initialize players (only now)
        Map.init_MAP()
        TronEntities.Tron_INIT()
        TronEntities.Clu_INIT()

        # Start game loop
        GameFunctions.game_Loop()
    else:
        print("Game over")

def mMenu():
    global current_option
    def draw_menu():
        pen.clear()
        pen.penup()
        pen.goto(0, 150)
        pen.write("TRON", align="center", font=("Courier", 80, "bold"))

        pen.goto(0, 50)
        if current_option == 0:
            pen.write("> Single Player", align="center", font=("Courier", 32, "bold"))
        else:
            pen.write("Single Player", align="center", font=("Courier", 32, "bold"))

        pen.goto(0, 0)
        if current_option == 1:
            pen.write("> Two Players", align="center", font=("Courier", 32, "bold"))
        else:
            pen.write("Two Players", align="center", font=("Courier", 32, "bold"))

        screen.update()

    def move_up():
        global current_option
        current_option = (current_option - 1) % 2
        draw_menu()

    def move_down():
        global current_option
        current_option = (current_option + 1) % 2
        draw_menu()

    def start_game():
        if current_option == 0:
            print("No Singleplayer Yet")
        elif current_option == 1:
            runGame()

    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(start_game, "Return")
    screen.listen()
    draw_menu()

# Show menu
mMenu()
screen.mainloop()