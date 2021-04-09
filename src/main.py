import turtle
import random
import math
from tkinter import messagebox
import pathlib
import sys
import winsound

# Creating the window to display maze

win = turtle.Screen()
win.bgcolor("#808080")
win.title("Maze game")
win.setup(width=700, height=700)
win.tracer(0)
grid_block_size = 24
screen = turtle.Screen()

# Register shapes
turtle.register_shape("Sprites/brick.gif")
turtle.register_shape("Sprites/brick1.gif")
turtle.register_shape("Sprites/coins.gif")
turtle.register_shape("Sprites/person.gif")
turtle.register_shape("Sprites/door.gif")
turtle.register_shape("Sprites/B.gif")
turtle.register_shape("Sprites/ClosedTreasure.gif")
turtle.register_shape("Sprites/enemy.gif")
turtle.register_shape("Sprites/GameOverBackground.gif")
turtle.register_shape("Sprites/OpenTreasure.gif")
turtle.register_shape("Sprites/wizz_left.gif")
turtle.register_shape("Sprites/wizz_right.gif")


# Creating blocks class
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.name = 'Wall'


# Creating player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        # self.shape(Player_Skeleton)
        self.shape("Sprites/enemy.gif")
        # self.color('red')
        self.penup()
        self.speed(0)
        self.points = 0
        self.lives = 3

    def take_next_step(self, next_x, next_y):
        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)

    def move_up(self):
        self.take_next_step(self.xcor(), self.ycor() + 24)
        # self.shape(Player_Up)

    def move_down(self):
        self.take_next_step(self.xcor(), self.ycor() - 24)
        # self.shape(Player_Down)

    def move_right(self):
        self.take_next_step(self.xcor() + 24, self.ycor())
        # self.shape(Player_Right)

    def move_left(self):
        self.take_next_step(self.xcor() - 24, self.ycor())
        # self.shape(Player_Left)

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
        self.shape("Sprites/ClosedTreasure.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.destroy


class Exit(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)

    def isLevelDone(self):
        win.clearscreen()
        win.resetscreen()
        win.bgpic("Sprites/B.gif")
        win.tracer(0)

class Lives(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(100, 320)
        self.hideturtle()
        self.lifecount = 'Lives Remaining: {}'.format(player.lives)

    def showLives(self):
        self.write(self.lifecount, False, align='left', font=('Times New Roman', 14, 'bold'))

class Points(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(-300, 320)
        self.hideturtle()

    def showPoints(self):
        self.write('Points: {}'.format(player.points), False, align='left', font=('Times New Roman', 14, 'bold'))

    def showLevel(self):
        self.setposition(-80, 320)
        self.write('Level 1', False, align='left', font=('Times New Roman', 14, 'bold'))

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Sprites/wizz_left.gif")
        self.penup()
        self.speed(0)
        self.points = 20
        self.goto(x, y)
        self.direction = random.choice(("L", "R", "U", "D"))
        if self.direction == "L":
            self.shape("Sprites/wizz_left.gif")
        elif self.direction == "R":
            self.shape("Sprites/wizz_right.gif")

    def move_enemy(self):
        next_x = self.xcor() + 24*(self.direction == "L")\
                 - 24*(self.direction == "R")
        next_y = self.ycor() + 24*(self.direction == "U")\
            - 24*(self.direction == "D")

        if (next_x, next_y) not in walls:
            self.goto(next_x, next_y)
        else:
            self.direction = random.choice(("L", "R", "U", "D"))
        turtle.ontimer(self.move_enemy, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Creating map setup function
def setup_maze(level):

    livesBox.showLives()


    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            x_coordinate = -288 + (x * 24)
            y_coordinate = 288 - (y * 24)

            if character == 'X':
                block.goto(x_coordinate, y_coordinate)
                block.stamp()
                walls.append((x_coordinate, y_coordinate))

            if character == 'P':
                player.goto(x_coordinate, y_coordinate)

            if character == 'T':
                reward = random.choice(('Gold', 'Silver', 'Bronze'))
                if reward == 'Gold':
                    Treasure.points = 100
                elif reward == 'Silver':
                    Treasure.points = 60
                elif reward == 'Bronze':
                    Treasure.points = 30
                treasure.append(Treasure(x_coordinate, y_coordinate))

            if character == 'E':
                enemies.append(Enemy(x_coordinate, y_coordinate))

            if character == 'I':
                exit.goto(x_coordinate, y_coordinate)
                exit.x_cor, exit.y_cor = x_coordinate, y_coordinate
                walls.append((exit.x_cor, exit.y_cor))


# Creating first map
def setup_level(level):

    setup_maze(levels[level])

    win.onkey(player.move_down, "Down")
    win.onkey(player.move_up, "Up")
    win.onkey(player.move_left, "Left")
    win.onkey(player.move_right, "Right")
    win.listen()

    for enemy in enemies:
        turtle.ontimer(enemy.move_enemy, t=120)

block = Wall()
player = Player()
livesBox = Lives()
pointsBox = Points()
textbox = Points()
exit = Exit()
treasure = []
enemies = []
walls = []
levels = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP       X     X    E   X",
    "XXXXXXX  X  X  X  XXXX  X",
    "X        X EX  X  X  X  X",
    "X  X  XXXXXXX  X  X  X  X",
    "X  X  X     X  X  X     X",
    "X  XXXX  X  X  X  XXXXXXX",
    "X  X     X     X        X",
    "X  X  XXXXXXXXXXXXXXXX  X",
    "X     X             E   X",
    "X  XXXX  X  XXXXXXXXXX  X",
    "X  X  X  X  X     X     X",
    "X  X  X  X  XXXX  X  XXXX",
    "X  XE    X     X        X",
    "X  XXXX  XXXX  XXXXXXX  X",
    "X     X     X       EX  X",
    "XXXX  XXXXXXX  XXXX  XXXX",
    "X TX E      X  XE X     X",
    "X  XXXXXXX  X  X  XXXX  X",
    "X  X       TX     X     X",
    "X  X  XXXXXXXXXXXXX  X  X",
    "X     X     X       TX  X",
    "X  XXXX  X  X  XXXXXXX  X",
    "X     E  X     X        I",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "I          EX           X",
    "X  XXXXXXX  XXXXXXXXXX  X",
    "X       EX     X     X  X",
    "X  XXXX  XXXX  X  X  X  X",
    "X  X  XE X  X     X    TX",
    "X  X  X  X  XXXX  XXXXXXX",
    "X     X  X     X  XE    X",
    "X  XXXX  X  XXXX  XXXX  X",
    "X  X     XE       X     X",
    "XXXX  XXXXXXXXXX  X  XXXX",
    "X     X        X  X  X  X",
    "X  X  X       TX  X  X  X",
    "XE X  XXXX  XXXX  X  X  X",
    "X  X        X     X     X",
    "X  X  XXXXXXX  XXXXXXX  X",
    "X  X     XT         EX  X",
    "X  XXXX  XXXXXXXXXXXXX  X",
    "X       E            X  X",
    "XXXXXXX  X  XXXXXXX     X",
    "X        X     X  X    TX",
    "X  XXXXXXXXXX  X  XXXXXXX",
    "XP                    E X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)



setup_level(1)
textbox.showLevel()

while True:

    if len(treasure) == 0:
        if (exit.xcor(), exit.ycor()) in walls:
            walls.remove((exit.xcor(), exit.ycor()))
        if player.is_collision(exit):
            win.clearscreen()
            win.resetscreen()
            win.tracer(0)
            win.bgpic("Sprites/B.gif")
            player = Player()
            block = Wall()
            livesBox = Lives()
            pointsBox = Points()
            exit = Exit()
            textbox = Points()
            treasure = []
            enemies = []
            walls = []
            setup_level(2)

    for reward in treasure:

        if player.is_collision(reward):
            reward.shape("Sprites/OpenTreasure.gif")
            player.points += reward.points
            # if reward.points == 100:
                # turtle.write('Gold Acquired!', False, align='center', font=('Times New Roman', 60, 'bold'))
            pointsBox.clear()
            pointsBox.showPoints()
            print("Player Points: {}".format(player.points))
            treasure.remove(reward)

    for enemy in enemies:

        if player.is_collision(enemy):
            player.lives -= 1
            livesBox.lifecount = 'Lives Remaining: {}'.format(player.lives)
            livesBox.clear()
            livesBox.showLives()
            enemy.destroy()

            if player.lives == 0:
                print("Player Dead")
                win.clearscreen()
                win.bgpic("Sprites/GameOverBackground.gif")
                turtle.hideturtle()
                turtle.color('white')
                turtle.write('Game Over', False, align='center', font=('Times New Roman', 50, 'bold'))

    win.update()




