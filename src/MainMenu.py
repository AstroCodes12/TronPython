import turtle
import GameFunctions
import Map
import State_Controls
import TronEntities


screen = Map.screen
screen.setup(width=800, height=600)
screen.title("TRON game")
screen.bgcolor("black")


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pencolor("cyan")

current_option = 0  # 0 = Single Player, 1 = Two Players

def mMenu():
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
        if current_option == 1:
            print("Two player")
            
            TronEntities.game_State = True
            screen.reset()
            State_Controls.runGame()
                
                
    print(TronEntities.game_State)

    draw_menu()
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(start_game, "Return")    