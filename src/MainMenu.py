import turtle
import GameFunctions
import Map
import State_Controls
import TronEntities
import ScoreMgr

pen = None

screen = Map.screen
screen.setup(width=750, height=750)
screen.title("TRON game")
screen.bgcolor("black")

current_option = 0  # 0 = Check Score, 1 = Start


def mMenu():
    global pen
    screen.setup(width=750, height=750)
    screen.title("TRON game")
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pencolor("cyan")

    def draw_menu():
        pen.clear()
        pen.penup()
        pen.goto(0, 150)
        pen.write("TRON", align="center", font=("Courier", 80, "bold"))

        pen.goto(0, 50)
        if current_option == 0:
            pen.write("> CHECK SCORE", align="center", font=("Courier", 32, "bold"))
        else:
            pen.write("CHECK SCORE", align="center", font=("Courier", 32, "bold"))

        pen.goto(0, 0)
        if current_option == 1:
            pen.write("> START", align="center", font=("Courier", 32, "bold"))
        else:
            pen.write("START", align="center", font=("Courier", 32, "bold"))
        screen.update()

    def draw_scores():
        """Display the scores from the file"""
        pen.clear()
        pen.penup()
        pen.goto(0, 200)
        pen.write("SCORES", align="center", font=("Courier", 60, "bold"))

        # Read scores from file
        scores = ScoreMgr.read_scores()

        pen.goto(0, 100)
        pen.pencolor("blue")
        pen.write(f"TRON: {scores.get('Tron', 0)}", align="center", font=("Courier", 40, "bold"))

        pen.goto(0, 30)
        pen.pencolor("red")
        pen.write(f"CLU: {scores.get('Clu', 0)}", align="center", font=("Courier", 40, "bold"))

        pen.goto(0, -50)
        pen.pencolor("cyan")
        pen.write("Press SPACE to return", align="center", font=("Courier", 20, "normal"))

        screen.update()

    def move_up():
        global current_option
        current_option = (current_option - 1) % 2
        draw_menu()

    def move_down():
        global current_option
        current_option = (current_option + 1) % 2
        draw_menu()

    def return_to_menu():
        """Return from score screen to main menu"""
        pen.pencolor("cyan")  # Reset color
        screen.onkey(None, "space")  # Unbind space
        draw_menu()
        # Re-bind menu controls
        screen.onkey(move_up, "Up")
        screen.onkey(move_down, "Down")
        screen.onkey(select_option, "Return")

    def select_option():
        """Selects either check score or start"""
        if current_option == 0:
            print("Check Scores")
            # Unbind menu keys
            screen.onkey(None, "Up")
            screen.onkey(None, "Down")
            screen.onkey(None, "Return")
            draw_scores()
            screen.onkey(return_to_menu, "space")

        if current_option == 1:
            print("Start")
            screen.onkey(None, "Up")
            screen.onkey(None, "Down")
            screen.onkey(None, "Return")

            # Clear and hide pen
            pen.clear()
            pen.hideturtle()
            pen.goto(10000, 10000)

            TronEntities.game_State = True
            State_Controls.runGame()

    print(TronEntities.game_State)

    draw_menu()
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(select_option, "Return")