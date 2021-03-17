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
turtle.register_shape("Images/brick.gif")
turtle.register_shape("Images/brick1.gif")
turtle.register_shape("Images/coins.gif")
turtle.register_shape("Images/person.gif")
turtle.register_shape("Images/door.gif")


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
        self.shape("Images/person.gif")
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
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Images/coins.gif")
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
        self.shape("Images/door.gif")
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
        self.shape("circle")
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

        win.ontimer(self.move, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Creating first map
map = [""]
map_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP       XXXXXT  XXXXXXXX",
    "XXXXX    XXXXX   XXXXXXXX",
    "XXXXX    XXXXX   XXXXXXXX",
    "XX                      X",
    "XX          XXXXX  XXXXXX",
    "XX          XXXXX  XX  XX",
    "XX             XX  XX  XX",
    "XX          XXXXX  XX  XX",
    "XX   XXXX   XXXXX  XX  XX",
    "XX   XXXX              XX",
    "XX   XXXX   XXXXXXXXT  XX",
    "XX E XXXX   XXXXXXXX   XX",
    "XXXXXXXXX   XXXXXXXX   XX",
    "XXXXXXXXX        XXXXXXXX",
    "X                      XX",
    "X  XX   XXXXXXXXXXX    XX",
    "X  XX   XXXXX   XXX    XX",
    "X  XX   XXXXX   XXX    XX",
    "XXXXX   XXXXX          XX",
    "XXXXX   XXXXX    XXX    G",
    "XXXXX            XXXXXXXX",
    "XX      XXXXXX   XXXXXXXX",
    "XX      XXXXXX        XXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_2 = [
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

# Append map
map.append(map_1)
map.append(map_2)


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

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            # Check if it is E representing enemies
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            # Check if it is G representing gate
            if character == "G":
                gates.append(Gate(screen_x, screen_y))


# Create enemies
enemies = []

# Creating Gates
gates = []

# Create treasure
treasures = []

# Setup maze map
setup_maze(map[1])
setup_maze(map[2])

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

# Moving enemies
for enemy in enemies:
    win.ontimer(enemy.move, t=250)

win.tracer(0)

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
            blocks.clear()

        if maze == ("map1"):
            setup_maze(map[2])
            maze = ("map2")
        else:
            turtle.bye()

turtle.done()
