import turtle
import Map
from pynput import keyboard
import threading
import math


Tron_Trail = []
Clu_Trail = []

screen = Map.screen # Screen Init

game_State = False #Game on / off

def Tron_INIT():
    """Defines Tron Player"""
    global Tron, Tron_Trail
    Tron = turtle.Turtle("square")
    Tron.color("blue")
    Tron.pensize(10)
    Tron.penup()
    Tron.goto(-200, 0)
    Tron.pendown()
    Tron.setheading(0)
    # reset trail
    Tron_Trail = []

def Clu_INIT():
    """Defines Clu Player"""
    global Clu, Clu_Trail
    Clu = turtle.Turtle("square")
    Clu.color("red")
    Clu.pensize(10)
    Clu.penup()
    Clu.goto(200, 0)
    Clu.pendown()
    Clu.setheading(180)
    # reset trail
    Clu_Trail = []