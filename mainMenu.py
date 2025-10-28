import turtle

def mMenu():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("TRON game")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    pen.penup()
    pen.goto(0, 200)
    pen.pendown()
    pen.write("TRON", align="center", font=("Courier", 52, "bold"))
    turtle.exitonclick()

mMenu()