import turtle
import random
import math


win = turtle.Screen()
win.bgcolor('red')
win.title('Simple Turtle game which uses Classes')
win.bgpic('kylo.gif')

class GameScore(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write('Score: {}'.format(self.score), False, align='left', font=('Arial', 14, 'normal'))

    def change_score(self, points):
        self.score += points
        self.update_score()



class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape('triangle')
        self.color('white')
        self.speed = 1

    # You shall not pass! behind borders...
    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def accelerates(self):
        self.speed += 1


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color('green')
        self.shape('circle')
        self.speed = 0.5
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


# collision between circle and triangle
def is_collision(p1, p2):
    a = p1.xcor() - p2.xcor()
    b = p1.ycor() - p2.ycor()
    distance = math.sqrt((a**2)+(b**2))

    if distance < 20:
        return True
    else:
        return False



# class create instance and border
player = Player()
border = Border()
game_score = GameScore()

# draw border
border.draw_border()

# moves with keys binding
turtle.listen()
turtle.onkey(player.turnleft, 'Left')
turtle.onkey(player.turnright, 'Right')
turtle.onkey(player.accelerates, 'Up')

# smoothing tracer
win.tracer(0)
# making multiple goals
goals = []
for item in range(5):
    goals.append(Goal())

while True:
    win.update()
    player.move()

    for goal in goals:
        goal.move()

        if is_collision(player, goal):
            goal.jump()
            game_score.change_score(1)

