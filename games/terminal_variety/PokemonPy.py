import random


class Pokemon:

    def __init__(self, name, element, health, speed):
        self.name = name
        self.element = element

        self.current_health = health
        self.max_health = health

        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        damage = random.randint(15, 25)
        print('Pokemon {} used {}'.format(self.name, self.moves[0]))
        print('It dealt {} damage.'.format(damage))
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        damage = random.randint(0, 50)
        print('Pokemon {} used {}'.format(self.name, self.moves[1]))
        if damage < 10:
            print('Attack missed')
        else:
            print('It dealt {} damage.'.format(damage))
            enemy.current_health -= damage

    def restore(self):
        heal = random.randint(15, 25)
        print('Pokemon {} used {}'.format(self.name, self.moves[2]))
        print('It healed {} damage.'.format(heal))
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print('Pokemon {} has fainted'.format(self.name))
            input('Press Enter to continue...')

    def show_stats(self):
        print('\n Name: {}'.format(self.name))
        print(' Element: {}'.format(self.element))
        print(' Current Health: {}/{}'.format(self.current_health, self.max_health))
        print(' Speed: {}'.format(self.speed))


class Fire(Pokemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']

    def special_attack(self, enemy):
        print('Pokemon {} used {}'.format(self.name, self.moves[3].upper()))

        if enemy.element == 'GRASS':
            print('Attack is super effective')
            damage = random.randint(35, 60)
        elif enemy.element == 'WATER':
            print('Attack is not effective')
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        enemy.current_health -= damage

    def move_info(self):
        print('\nPokemon: {} Moves:'.format(self.name))
        print('Attack type: {}'.format(self.moves[0]))
        print('Heavy Attack type: {}'.format(self.moves[1]))
        print('Heal type: {}'.format(self.moves[2]))
        print('Special Attack type: {}'.format(self.moves[3]))


class Water(Pokemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Bite', 'Splash', 'Dive', 'Water Blast']

    def special_attack(self, enemy):
        print('Pokemon {} used {}'.format(self.name, self.moves[3].upper()))

        if enemy.element == 'FIRE':
            print('Attack is super effective')
            damage = random.randint(35, 60)
        elif enemy.element == 'GRASS':
            print('Attack is not effective')
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        enemy.current_health -= damage

    def move_info(self):
        print('\nPokemon: {} Moves:'.format(self.name))
        print('Attack type: {}'.format(self.moves[0]))
        print('Heavy Attack type: {}'.format(self.moves[1]))
        print('Heal type: {}'.format(self.moves[2]))
        print('Special Attack type: {}'.format(self.moves[3]))


class Grass(Pokemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['WineWip', 'Grab', 'Grow', 'Slice']

    def special_attack(self, enemy):
        print('Pokemon {} used {}'.format(self.name, self.moves[3].upper()))

        if enemy.element == 'WATER':
            print('Attack is super effective')
            damage = random.randint(35, 60)
        elif enemy.element == 'FIRE':
            print('Attack is not effective')
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        enemy.current_health -= damage

    def move_info(self):
        print('\nPokemon: {} Moves:'.format(self.name))
        print('Attack type: {}'.format(self.moves[0]))
        print('Heavy Attack type: {}'.format(self.moves[1]))
        print('Heal type: {}'.format(self.moves[2]))
        print('Special Attack type: {}'.format(self.moves[3]))


class Game:
    def __init__(self):
        self.pokemon_elements = ['FIRE', 'WATER', 'GRASS']
        self.pokemon_names = ['Chewdie', 'Spatula', "Montego", 'Marmander', 'PikaPika', 'Czu czu', 'Grey worm'
                                                                                                   'Spider', 'Lion',
                              'Tiger', 'Watermelon', 'Gigantosaur', 'TakiTomek', 'Grazyna']
        self.battles_won = 0

    def create_pokemnon(self):
        health = random.randint(70, 100)
        speed = random.randint(1, 10)

        element = self.pokemon_elements[random.randint(0, len(self.pokemon_elements) - 1)]
        name = self.pokemon_names[random.randint(0, len(self.pokemon_names) - 1)]

        if element == 'FIRE':
            pokemon = Fire(name, element, health, speed)
        elif element == 'WATER':
            pokemon = Water(name, element, health, speed)
        else:
            pokemon = Grass(name, element, health, speed)

        return pokemon

    def choose_pokemon(self):
        starters = []
        while len(starters) < 3:
            pokemon = self.create_pokemnon()
            valid_pokemon = True
            for starter in starters:
                if starter.name == pokemon.name or starter.element == pokemon.element:
                    valid_pokemon = False
            if valid_pokemon:
                starters.append(pokemon)
        for starter in starters:
            starter.show_stats()
            starter.move_info()

        print('Choose your pokemon')
        print('1. {}'.format(starters[0].name))
        print('2. {}'.format(starters[1].name))
        print('3. {}'.format(starters[2].name))
        choice = int(input('Tell me then number'))

        pokemon = starters[(choice - 1)]
        return pokemon

    def get_attack(self, pokemon):
        print('What would you like to do?')
        print('1. {}'.format(pokemon.moves[0]))
        print('2. {}'.format(pokemon.moves[1]))
        print('3. {}'.format(pokemon.moves[2]))
        print('4. {}'.format(pokemon.moves[3]))
        choice = int(input('Tell me then number of action'))

        return choice

    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        computer.faint()

    # It would be great to implement AI to Computer moves instead of randomizing it
    def computer_attack(self, player, computer):
        move = random.randint(1, 4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)

        player.faint()

    def battle(self, player, computer):
        move = self.get_attack(player)

        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)

print('Welcome. There You have Pokemon game')
input('Press Enter to start playing')

player_main = True

while player_main:
    game = Game()
    player = game.choose_pokemon()
    print('Gratz! You choose {} as your first pokemon. \n Now press Enter to play' .format(player.name))
    while player.is_alive:
        computer = game.create_pokemnon()
        print('A wild pokemon {} approached'.format(computer.name))
        computer.show_stats()

        while computer.is_alive and player.is_alive:
            game.battle(player, computer)
            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()
                print('--------------------------------')
        if player.is_alive:
            game.battles_won += 1
    print('Poor {} has fainted but won {} battles'. format(player.name, game.battles_won))
    choice = input('Do you want to play more?y or n').upper()
    if choice != 'Y':
        player_main = False
        print('Thanks for playing')

        
    

