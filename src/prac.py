import turtle
import math
import random
from tkinter import messagebox
import winsound
import sys

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Maze Game")
wn.setup(700, 700)
wn.tracer(0)

# Play Sound
winsound.PlaySound("Maze_Music", winsound.SND_ASYNC)

# Register shapes
turtle.register_shape("Jake_Guy.gif")
turtle.register_shape("Cobble_Moss.gif")
turtle.register_shape("Chest_Treasure.gif")
turtle.register_shape("Thing_Right.gif")
turtle.register_shape("Thing_Left.gif")
turtle.register_shape("Exit_Door.gif")


# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        messagebox.showinfo("Story", "Jake is an explorer that wanders around the world."
                                     "He then saw a cave which caught his attention."
                                     "The cave has maze like walls and it is known to "
                                     "posses treasures, but Jake was not aware that there"
                                     "are monsters lurking around.")
        messagebox.showinfo("GamePlay", "Coins = 200 \n Grand Treasure = 1000")
        messagebox.showinfo("Keybinds", "Use up down right leftt arrow keys to move")


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Jake_Guy.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

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
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Chest_Treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Gate(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Exit_Door.gif")
        self.color("pink")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Thing_Left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("Thing_Left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("Thing_Right.gif")
        else:
            dx = 0
            dy = 0

        # Calculate the movement spot of enemy
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        wn.ontimer(self.move, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Create Levels
levels = [""]
# Define first
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XT E     XXXXX G XXXXXXXX",
    "XXXXX    XXXXX   XXXXXXXX",
    "XXXXX    XXXXX   XXXXXXXX",
    "XX                     EX",
    "XX          XXXXX  XXXXXX",
    "XX          XXXXX  XX EXX",
    "XXT            EX  XX  XX",
    "XX          XXXXX  XX  XX",
    "XX     XX   XXXXX  XX  XX",
    "XX E   XX              XX",
    "XX     XX     XXXXXXX  XX",
    "XX T   XX    TXXXXXXX  XX",
    "XXXXXXXXX   XXXXXXX E  XX",
    "XXXXXXXXX        XXXXXXXX",
    "X                     EXX",
    "X  XX     XXXXXXXXX    XX",
    "X  XX     XXX E  XX    XX",
    "XE XX    TXXX    XX    XX",
    "XXXXX   XXXXX          XX",
    "XXXXX   XXXXX    XX   EXX",
    "XXXXX              XXXXXX",
    "XX      XXXXXX     XXXXXX",
    "XX P    XXXXXX   T  E XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXX   P   XXX",
    "X E XXXXXXXXXXX       XXX",
    "X      XXXXXXX    XXXXXXX",
    "X                XXXXXXXX",
    "X      XXXXXXX XXXXXXXXXX",
    "XXXX   XXXXXE      XXXXXX",
    "XXXX   XXXXXXXXX   XXXXXX",
    "XE                   EXXX",
    "X     XXXXXXXXXXXX    XXX",
    "XXXX XXXXXXXXXXXXX    XXX",
    "XXX             XX    XXX",
    "XXXE            XX    XXX",
    "XXXXXXXX        XX   EXXX",
    "XE           XXXXX  XXXXX",
    "X      XXXXXXXXXXX      X",
    "XXXXX  XXXXXXXXXXE      X",
    "XXXXX      XXXXXXXXXX   X",
    "XXXXX          XXXXXX   X",
    "XXXXXXXXXX              X",
    "XXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXX            XXXXXXX",
    "XXXXXX E     XXXXXXXXXXXXX",
    "XXXXXXXX              T X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasure to list
treasures = []

# Add Gate to List
gates = []

# Add Enemies to list
enemies = []

# Add maze to list
levels.append(level_1)
levels.append(level_2)


# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X representing a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("Cobble_Moss.gif")
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check if it is a P representing the Player
            if character == "P":
                player.goto(screen_x, screen_y)

            # Check if it is a T representing Treasure
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            # Check if it is E representing enemies
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            # Check if it is G representing gate
            if character == "G":
                gates.append(Gate(screen_x, screen_y))


# Create class instance
pen = Pen()
player = Player()

# Create Wall
walls = []

# Set up the level
setup_maze(levels[1])
setup_maze(levels[2])

# Keyboard Binds
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Moving enemies
for enemy in enemies:
    wn.ontimer(enemy.move, t=250)

# Turn off screen updates
wn.tracer(0)

# Main loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold {}.".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

            # Player when colliding with enemy
    for enemy in enemies:
        if player.is_collision(enemy):
            messagebox.showinfo("Info", "You Died, Please press OK and Start the game again")
            exit()
            # Player when Colliding with Gate
    for gate in gates:
        if player.is_collision(gate):
            messagebox.showinfo("Congratulations", "You reached the first gate")
        pen.clear()

        if maze == ("level1"):
            setup_maze(levels[2])
            maze = ("level2")
        else:
            turtle.bye()

    wn.update()
