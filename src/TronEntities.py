import turtle
import Map
from pynput import keyboard
import threading
import math


Tron_Trail = []

Clu_Trail = []

screen = Map.screen # Screen Init
<<<<<<< HEAD
game_State = True # Game on / off
=======

game_State = False #Game on / off
>>>>>>> 0ad9867 (Changed main menu to be navigate into the box to start. Menu to game and back to menu works, when configured this way)

"""Entity INIT"""
Tron = turtle.Turtle("square")

def Tron_INIT():
    global Tron
    Tron.color("blue")
    Tron.pensize(10)
    Tron.penup()
    Tron.goto(-200, 0)
    Tron.pendown()
    Tron.setheading(0)

Clu = turtle.Turtle("square")

def Clu_INIT():
    global Clu
    Clu.color("red")
    Clu.pensize(10)
    Clu.penup()
    Clu.goto(200, 0)
    Clu.pendown()
    Clu.setheading(180)
