import turtle
import sys
from tkinter import *

images = ['Images/wall.gif']



#Creating the window to display maze
win = turtle.Screen()
win.title("Maze game")
win.bgcolor("grey")
win.setup(width= 900,height= 900)
win.tracer(0)
for image in images:
    win.register_shape(image)

#Creating blocks class
class Blocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('Images/wall.gif')
        self.penup()
        self.speed(0)

#Creting first map
map = [""]
map_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX     XXXXXXXXXXXXXXXXXXXXXX",
"XXX     XXXXXXXXXXXXXXXXXXXXXX",
"XXX         XXXXXXXXXXXXXXXXXX",
"XXXXXXX     XXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]














blocks = Blocks()

turtle.done()