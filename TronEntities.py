import turtle
import Map
from pynput import keyboard
import threading
import math


Tron_x = []
Tron_y = []

Clu_x = []
Clu_y = []

screen = Map.screen # Screen Init
game_State = True 

"""Entity INIT"""
Tron = turtle.Turtle("arrow")

def  Tron_INIT():
    global Tron
    Tron.color("blue")
    Tron.pensize(10)
    Tron.penup()
    Tron.goto(-200, 0)
    Tron.pendown()
    Tron.setheading(0)

Clu = turtle.Turtle("arrow")

def Clu_INIT():
    global Clu
    Clu.color("red")
    Clu.pensize(10)
    Clu.penup()
    Clu.goto(200, 0)
    Clu.pendown()
    Clu.setheading(180)
