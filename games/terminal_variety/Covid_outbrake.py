import math
import random
import tkinter


class Simulation:
    def __init__(self):
        self.day_number = 1

        self.population_size = int(input('--Enter Population size'))
        root = math.sqrt(self.population_size)
        if int(root + 0.5) ** 2 != self.population_size:
            root = round(root, 0)
            self.grid_size = int(root)
            self.population_size = self.grid_size ** 2
        else:
            self.grid_size = int(math.sqrt(self.population_size))

        self.infection_percent = (float(input('--Enter the % of the population which is already infected'))) / 100
        self.infection_propability = (float(input('--Enter the propability that person will get infection'))) / 100
        self.infection_duration = int(input('--How many days will the infection last?'))
        self.mortality_rate = float(input('--What is mortality rate of infecion in %')) / 100

        self.sim_day = int(input('--How many days you want to check?'))


class Person:
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, simulation):
        if random.randint(0, 100) < simulation.infection_propability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def kill(self):
        self.is_dead = True

    def update(self, simualtion):
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                if random.randint(0, 100) < simualtion.mortality_rate:
                    self.kill()
                elif self.days_infected == simualtion.infection_duration:
                    self.heal()


class Populaton:
    def __init__(self, simulation):
        self.population = []
        for i in range(simulation.grid_size):
            row = []
            for person in range(simulation.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self, simulation):
        infected_count = int(round(simulation.infection_percent * simulation.population_size))
        infections = 0

        while infections < infected_count:
            x = random.randint(0, simulation.grid_size - 1)
            y = random.randint(0, simulation.grid_size - 1)

            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected += 1
                infections += 1

    def spread(self, simulation):
        for i in range(simulation.grid_size):
            for j in range(simulation.grid_size):
                if not self.population[i][j].is_dead:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j + 1].is_infected or self.population[i + 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            if self.population[i][j - 1].is_infected or self.population[i + 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or \
                                    self.population[i + 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    elif i == simulation.grid_size - 1:
                        if j == 0:
                            if self.population[i][j + 1].is_infected or self.population[i - 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            if self.population[i][j - 1].is_infected or self.population[i - 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or \
                                    self.population[i - 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    else:
                        if j == 0:
                            if self.population[i][j + 1].is_infected or self.population[i + 1][j].is_infected or \
                                    self.population[i + 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size - 1:
                            if self.population[i][j - 1].is_infected or self.population[i + 1][j] or \
                                    self.population[i - 1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j - 1].is_infected or self.population[i][j + 1].is_infected or \
                                    self.population[i + 1][j].is_infected or self.population[i - 1][j].is_infected:
                                self.population[i][j].infect(simulation)

    def update(self, simulation):
        simulation.day_number += 1
        for row in self.population:
            for person in row:
                person.update(simulation)

    def display_stat(self, simulation):
        total_infected_count = 0
        total_death_count = 0

        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected_count += 1
                    if person.is_dead:
                        total_death_count += 1

        infected_percent = round(100 * (total_infected_count / simulation.population_size), 4)
        death_percent = round(100 * total_death_count / simulation.population_size, 4)

        print('\n Day # {}'.format(simulation.day_number))
        print('Percent of infected population {} '.format(str(infected_percent)))
        print('Percent of dead population {} '.format(str(death_percent)))
        print('Total infected infected population {} '.format(str(total_infected_count)))
        print('Count of all dead  {} '.format(str(death_percent)))


def graphics(simulation, population, canvas):
    squere_dimension = 600 // simulation.grid_size
    for i in range(simulation.grid_size):
        y = i * squere_dimension
        for j in range(simulation.grid_size):
            x = j * squere_dimension
            if population.population[i][j].is_dead:
                canvas.create_rectangle(x, y, x + squere_dimension, y + squere_dimension, fill='red')
            else:
                if population.population[i][j].is_infected:
                    canvas.create_rectangle(x, y, x + squere_dimension, y + squere_dimension, fill='yellow')
                else:
                    canvas.create_rectangle(x, y, x + squere_dimension, y + squere_dimension, fill='green')


sim = Simulation()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

sim_window = tkinter.Tk()
sim_window.title('Covid Outbreak')
sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)

pop = Populaton(sim)

pop.initial_infection(sim)
pop.display_stat(sim)
input("Press Enter to start")

for i in range(1, sim.sim_day):
    pop.spread(sim)
    pop.update(sim)
    pop.display_stat(sim)
    graphics(sim, pop, sim_canvas)

    sim_window.update()

    if i != sim.sim_day - 1:
        sim_canvas.delete('all')
