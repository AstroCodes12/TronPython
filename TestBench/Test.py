import turtle
from pynput import keyboard
import threading

w_State = False
d_State = False
a_State = False

game_State = True

screen = turtle.Screen()

turt = turtle.Turtle("arrow")

turt.color("blue")

def Tkinter_Bye():
    global game_State

    game_State = False
    turtle.bye()
    print("Tkinter_Bye Called")


def on_press(key):
    global w_State
    global a_State
    global d_State
    global game_State
    try:
        if key == keyboard.KeyCode.from_char('w'):
            w_State = True
            print("W key pressed - w_State set to True")
        elif key == keyboard.KeyCode.from_char('d'):
            d_State = True
            print("D key pressed - d_State set to True")
        elif key == keyboard.KeyCode.from_char('a'):
            a_State = True
            print("A key pressed - a_State set to True")
    except AttributeError:
        pass

def on_release(key):
    global w_State
    global d_State
    global a_State
    global game_State
    try:
        if key == keyboard.KeyCode.from_char('w'):
            w_State = False
            print("W key released - w_State set to False")
        elif key == keyboard.KeyCode.from_char('d'):
            d_State = False  # Stop listener
            print("D key released - d_State set to False")
        elif key == keyboard.KeyCode.from_char('a'):
            a_State = False  # Stop listener
            print("A key released - a_State set to False")
    except AttributeError:
        pass


def game_loop(game_State=game_State):
    global w_State
    global d_State
    global a_State

    while game_State:
        screen.update()
        if w_State:
            turt.forward(10)
        elif a_State:
            turt.left(90)
        elif d_State:
            turt.right(90)
    

         
        



if game_State:
    pynput_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    pynput_listener_thread = threading.Thread(target=pynput_listener.start)
    pynput_listener_thread.daemon = True # Allow program to exit even if this thread is running
    pynput_listener_thread.start()


    game_loop()  # Start the game loop

    screen.onkey(Tkinter_Bye(), "Escape")
    screen.listen() #listens for 'esc'
else:
    print("Game Over") 