import turtle
import random
import math
from tkinter import messagebox
import sys
import winsound

# Creating the window to display maze

win = turtle.Screen()
win.title("Maze game")
win.bgcolor("grey")
win.setup(width=700, height=700)

# Register shapes
turtle.register_shape("Images/wall.gif")
turtle.register_shape("Images/brick.gif")
turtle.register_shape("Images/brick1.gif")


# Creating blocks class
class Blocks(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Images/brick1.gif")
        self.penup()
        self.speed(0)
        messagebox.showinfo("Story", "Welcome to an adventure"
                                     "To a scary adventure")


# Creating player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0

    # Player movement
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False
class Treasure(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")


# Creating first map
map = [""]
map_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP       XXXXX   XXXXXXXX",
    "XXXXX    XXXXX   XXXXXXXX",
    "XXXXX    XXXXX   XXXXXXXX",
    "XX                      X",
    "XX          XXXXX  XXXXXX",
    "XX          XXXXX  XX  XX",
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
    "X  XX    XXXX    XX    XX",
    "XXXXX   XXXXX          XX",
    "XXXXX   XXXXX    XX    XX",
    "XXXXX              XXXXXX",
    "XX      XXXXXX     XXXXXX",
    "XX      XXXXXX        XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Append map
map.append(map_1)


# Creating map setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X representing a wall
            if character == "X":
                blocks.goto(screen_x, screen_y)
                blocks.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)


# Create Walls
walls = []

# Creating class instance
blocks = Blocks()
player = Player()

# Keybinding
turtle.listen()
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")

# Setup maze map
setup_maze(map[1])

turtle.done()
