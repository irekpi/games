import os


class Board:
    def __init__(self):
        self.spots = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display(self):
        print(' {} | {} | {}'.format(self.spots[1], self.spots[2], self.spots[3]))
        print('-----------')
        print(' {} | {} | {}'.format(self.spots[4], self.spots[5], self.spots[6]))
        print('-----------')
        print(' {} | {} | {}'.format(self.spots[7], self.spots[8], self.spots[9]))

    def update(self, spot_no, value):
        if self.spots[spot_no] == ' ':
            self.spots[spot_no] = value

    def is_win(self, player):
        if self.spots[1] == player and self.spots[2] == player and self.spots[3] == player:
            return True
        if self.spots[4] == player and self.spots[5] == player and self.spots[6] == player:
            return True
        if self.spots[7] == player and self.spots[8] == player and self.spots[9] == player:
            return True
        if self.spots[1] == player and self.spots[4] == player and self.spots[7] == player:
            return True
        if self.spots[2] == player and self.spots[5] == player and self.spots[8] == player:
            return True
        if self.spots[3] == player and self.spots[6] == player and self.spots[9] == player:
            return True
        if self.spots[7] == player and self.spots[5] == player and self.spots[3] == player:
            return True
        if self.spots[1] == player and self.spots[5] == player and self.spots[9] == player:
            return True

    def reset(self):
        self.spots = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_tie(self):
        used_spots = 0
        for spot in self.spots:
            if spot != ' ':
                used_spots += 1
        if used_spots == 9:
            return True
        else:
            return False


board = Board()


def refresh_screen():
    os.system("clear")
    print('The Game!')
    board.display()


while True:
    refresh_screen()
    # making mvoe x
    mark_x = int(input('Which field you want to fill with X? 1 - 9 '))

    # board update
    board.update(mark_x, 'X')
    refresh_screen()

    if board.is_win('X'):
        print('X wins')
        play_again = input('Do you want to play again? Y/N? ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
    # check if Tie
    if board.is_tie():
        print('its Tie')
        play_again = input('Do you want to play again? Y/N? ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break

    # making mvoe o
    mark_o = int(input('Which field you want to fill with O? 1 - 9 '))

    # board update
    board.update(mark_o, 'O')
    refresh_screen()

    # checks if O won
    if board.is_win('O'):
        print('O wins')
        play_again = input('Do you want to play again? Y/N? ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break

    # check if Tie
    if board.is_tie():
        print('its Tie')
        play_again = input('Do you want to play again? Y/N? ').upper()
        if play_again == 'Y':
            board.reset()
            continue
        else:
            break
