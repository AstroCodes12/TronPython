import turtle

#Create Background
screen = turtle.Screen()
screen.setup(width=750, height=750)
screen.bgcolor("black")
screen.setworldcoordinates(-375, -375, 375, 375)  # make (0,0) the true visual center

#Create Border
border = turtle.Turtle()
border.color("cyan")
border.speed(0)
border.pensize(4)
border.penup()
border.goto(-350, -350)
border.pendown()

for _ in range(4):
    border.forward(700)
    border.left(90)

border.hideturtle()

#Create Grid Lines
grid = turtle.Turtle()
grid.speed(0)
grid.color("gray20")
grid.pensize(1)

#Vertical Lines
for x in range(-350, 351, 25):
    grid.penup()
    grid.goto(x, -350)
    grid.pendown()
    grid.goto(x, 350)

#Horizontal Lines
for y in range(-350, 351, 25):
    grid.penup()
    grid.goto(-350, y)
    grid.pendown()
    grid.goto(350, y)

grid.hideturtle()

# --- Create Player ---
player = turtle.Turtle()
player.shape("square")
player.color("lime")
player.penup()
player.goto(-12.5, 12.5)
player.setheading(0)  # start facing right

# --- Player Settings ---
step_size = 25  # moves one grid cell per step
move_delay = 75  # milliseconds between moves (controls speed)
direction = "up"  # current movement direction
alive = True

# --- Movement Functions ---
def go_up():
    global direction
    if direction != "down":  # prevent instant 180 turns
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# --- Game Loop (movement + border detection) ---
def move():
    global alive
    if not alive:
        return

    x, y = player.position()

    if direction == "up":
        y += step_size
    elif direction == "down":
        y -= step_size
    elif direction == "left":
        x -= step_size
    elif direction == "right":
        x += step_size

    # Border collision detection
    if x < -350 or x > 350 or y < -350 or y > 350:
        player.color("red")
        alive = False
        print("💀 Player crashed into the wall!")
        return

    player.goto(x, y)

    screen.update()
    screen.ontimer(move, move_delay)  # schedule next movement

# --- Keybindings ---
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- Start Game ---
move()
screen.mainloop()
