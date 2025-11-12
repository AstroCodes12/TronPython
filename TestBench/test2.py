import turtle

screen = turtle.Screen()
screen.tracer(0)

p1 = turtle.Turtle()
p2 = turtle.Turtle()

# Starting directions
p1_dx, p1_dy = 1, 0
p2_dx, p2_dy = -1, 0

# Keybindings
def p1_left():
    global p1_dx, p1_dy
    p1_dx, p1_dy = 0, 1

def p2_right():
    global p2_dx, p2_dy
    p2_dx, p2_dy = 1, 0

screen.listen()
screen.onkeypress(p1_left, "a")
screen.onkeypress(p2_right, "Right")

def game_loop():
    p1.setx(p1.xcor() + p1_dx)
    p1.sety(p1.ycor() + p1_dy)

    p2.setx(p2.xcor() + p2_dx)
    p2.sety(p2.ycor() + p2_dy)

    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()
