import turtle

def mMenu():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("TRON game")
    screen.bgcolor("black")

    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pencolor("cyan")

    current_option = 0  # 0 = Single Player, 1 = Two Players

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
        nonlocal current_option
        current_option = (current_option - 1) % 2
        draw_menu()

    def move_down():
        nonlocal current_option
        current_option = (current_option + 1) % 2
        draw_menu()

    draw_menu()
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")

    turtle.exitonclick()

mMenu()
