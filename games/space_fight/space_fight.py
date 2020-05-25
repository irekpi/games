import os
import turtle
import random
import time

turtle.speed(0)
turtle.bgcolor('black')
turtle.bgpic('kylo.gif')
turtle.ht()
turtle.title("SpaceFights")
turtle.setundobuffer(1)
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.fd(0)

        self.speed = 1

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
                (self.xcor() <= (other.xcor() + 20)) and \
                (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.5, outline=None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.speed = 20
        self.status = 'ready'
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == 'ready':
            os.system('aplay fire.wav&')
            self.goto(player.xcor(), player. ycor())
            self.setheading(player.heading())
            self.status = 'firing'

    def move(self):
        if self.status == 'ready':
            self.goto(-1000, 1000)

        if self.status == 'firing':
            self.fd(self.speed)
        # reload
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() > 290 or self.ycor() < -290:
            self.status = 'ready'


class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1
        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, 1000)


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = 'playing'
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color('white')
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = 'Score: {}'.format(self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, 'normal'))


# game
game = Game()
game.draw_border()
game.show_status()


# players
player = Player('triangle', 'white', 0, 0)
# enemy = Enemy('circle', 'red', -50, 0)
missile = Missile('triangle', 'yellow', 0, 0)
# ally = Ally('circle', 'blue', 30, 0)

enemies = []
for item in range(6):
    enemies.append(Enemy('circle', 'red', -50, 0))

allies = []
for item in range(6):
    allies.append(Ally('circle', 'blue', 40, 0))

particles = []
for item in range(20):
    particles.append(Particle('circle', 'yellow', 0, 0))
# keyboard
turtle.onkey(player.turn_left, 'Left')
turtle.onkey(player.turn_right, 'Right')
turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.decelerate, 'Down')
turtle.onkey(missile.fire, 'space')
turtle.listen()

while True:
    turtle.update()
    time.sleep(0.03)
    player.move()
    missile.move()

    for enemy in enemies:
        enemy.move()
        # collsion
        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score += 1
            game.show_status()

        if missile.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = 'ready'
            game.score += 1
            game.show_status()
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())

    for ally in allies:
        ally.move()
        # collsion
        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = 'ready'
            game.score -= 1
            game.show_status()
    for particle in particles:
        particle.move()



