import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    rows = 20
    width = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.position = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.position = (self.position[0] + self.dirnx, self.position[1] + self.dirny)

    def draw(self, surface, eyes=False):
        distance = self.width // self.rows
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(surface, self.color, (i * distance + 1, j * distance + 1, distance - 2, distance - 2))

        if eyes:
            centre = distance // 2
            radius = 3
            circle_middle = (i * distance + centre - radius, j * distance + 8)
            circle_middle2 = (i * distance + distance - radius * 2, j * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.position[0] <= 0:
                    c.position = (c.rows - 1, c.position[1])
                elif c.dirnx == 1 and c.position[0] >= c.rows - 1:
                    c.position = (0, c.position[1])
                elif c.dirny == 1 and c.position[1] >= c.rows - 1:
                    c.position = (c.position[0], 0)
                elif c.dirny == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, position):
        self.head = Cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.position[0] - 1, tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.position[0] + 1, tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.position[0], tail.position[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.position[0], tail.position[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid(width, rows, surface):
    size_betwen = width // rows

    x = 0
    y = 0

    for line in range(rows):
        x = x + size_betwen
        y = y + size_betwen
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def redraw_window(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break
    return x, y


def message_box(subject, content):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(rows, s), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].position == snack.position:
            s.add_cube()
            snack = Cube(random_snack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].position in list(map(lambda z: z.position, s.body[x + 1:])):
                print('Score:', len(s.body))
                message_box('You lost', 'try agian')
                s.reset((10, 10))
                break

        redraw_window(surface=win)


main()
