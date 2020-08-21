import random


class Creature:
    """Simple Tamagochi clone for fun!"""

    def __init__(self, name):
        self.name = name.title()

        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 0
        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.hunger -= random.randint(1, 4)
            print('Yummmm! {} had great meal!'.format(self.name))
        else:
            print('{} doesnt have any food'.format(self.name))
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        value = random.randint(0, 2)
        print('Do you want to play a game? Guess the number form 0 to 2')
        guess = int(input('Take a guess!'))

        if value == guess:
            print('Thats correct')
            self.boredom -= 3
        else:
            print('WRONG. The correct num was {}'.format(value))
            self.boredom -= 1

        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 2
        print('ZzzzZzzz. {} is sleeping'.format(self.name))

        if self.boredom < 0:
            self.boredom = 0
        if self.tiredness < 0:
            self.tiredness = 0

    def awake(self):
        value = random.randint(0, 2)
        if value == 0:
            print('{} is UP'.format(self.name))
            self.tiredness = 0
            self.is_sleeping = False
        else:
            print('{} wont wake up'.format(self.name))
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print('{} is all CLEAN!'.format(self.name))

    def forage(self):
        food_found = random.randint(0, 4)
        self.food += food_found
        self.dirtiness += 2
        print(('{} found {} pieces of food'.format(self.name, food_found)))

    def show_values(self):
        print('\nCreature name: {}'.format(self.name))
        print('Hunger (0-10): {}'.format(self.hunger))
        print('Boredom (0-10): {}'.format(self.boredom))
        print('Tiredness (0-10): {}'.format(self.tiredness))
        print('Dirtiness (0-10): {}'.format(self.dirtiness))
        print('Food pieces: {}'.format(self.food))
        if self.is_sleeping:
            print('\n{} is sleeping'.format(self.name))
        else:
            print('\n{} is awake!'.format(self.name))

    def incremet_values(self, difficulty):
        self.hunger += random.randint(0, difficulty)
        self.dirtiness += random.randint(0, difficulty)

        if self.is_sleeping == False:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)

    def kill(self):
        if self.hunger >= 10:
            print('{} has straved to death'.format(self.name))
            self.is_alive = False
        elif self.dirtiness >= 10:
            print('{} died from worms...'.format(self.name))
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print('{} is bored and went to sleep...'.format(self.name))
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print('{} is way to tired went to sleep...'.format(self.name))
            self.is_sleeping = True


def show_menu(creature):
    if creature.is_sleeping:
        choice = input('Enter 6 to try waking up creature!')
        choice = '6'
    else:
        print('\nEnter 1 to eat!')
        print('Enter 2 to play!')
        print('Enter 3 to sleep!')
        print('Enter 4 to take bath!')
        print('Enter 5 to forage for food!')
        choice = input('Chose what to do?')
    return choice


def call_action(creature, choice):
    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice == '6':
        creature.awake()
    else:
        print('Sorry that is not a valid move :(')


print('Welcome To Python Tamagochi game')
diff = int(input('Tell me the difficulty on which You would like to play? (1-5)'))

if diff > 5:
    diff = 5
elif diff < 1:
    diff = 1

running = True
while running:
    name = input('Choose name for your pet')
    player = Creature(name)
    rounds = 1
    while player.is_alive:
        print('\n--------------------')
        print('Round nr {}'.format(rounds))

        player.show_values()
        round_move = show_menu(player)
        call_action(player, round_move)

        print('Round {} summary'.format(rounds))
        player.show_values()
        input('Press Enter to continue...')

        player.incremet_values(diff)
        player.kill()
        rounds += 1
    print('RIP')
    print('Creature survived {}'.format(rounds))
    choice = input('Would you liketo play again? Y to continue').title()
    if choice != 'Y':
        running = False
        print('Bye Bye!')
