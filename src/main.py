import turtle
import random
import math
from tkinter import *
import sys
import winsound

# Creating the window to display maze
win = turtle.Screen()
win.title("Maze game")
win.bgcolor("grey")
win.setup(width=900, height=900)


#Register shapes
turtle.register_shape("Images/wall.gif")

# Creating blocks class
class Blocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Images/wall.gif")
        self.penup()
        self.speed(0)


# Creating first map
map = [""]
map_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X        XXXXX   XXXXXXXX",
"XXXXX    XXXXX   XXXXXXXX",
"XXXXX    XXXXX   XXXXXXXX",
"XX                      X",
"XX          XXXXX  XXXXXX",
"XX          XXXXX  XX EXX",
"XX              X  XX  XX",
"XX          XXXXX  XX  XX",
"XX     XX   XXXXX  XX  XX",
"XX     XX              XX",
"XX     XX     XXXXXXX  XX",
"XX     XX    TXXXXXXX  XX",
"XXXXXXXXX   XXXXXXX    XX",
"XXXXXXXXX        XXXXXXXX",
"X                      XX",
"X  XX     XXXXXXXXX    XX",
"X  XX     XXX    XX    XX",
"X  XX    TXXX    XX    XX",
"XXXXX   XXXXX          XX",
"XXXXX   XXXXX    XX    XX",
"XXXXX              XXXXXX",
"XX      XXXXXX     XXXXXX",
"XX      XXXXXX        XXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Creating map setup function
def setup_maze(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            player = map[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if player == "X":
                blocks.goto(screen_x, screen_y)
                blocks.stamp()

#Append map
map.append(map_1)

#Creating class instance
blocks = Blocks()

#Setup maze map
setup_maze(map[1])

turtle.done()
