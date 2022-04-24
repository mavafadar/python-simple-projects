from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from game import TicTacToe

import time

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = x_player.letter
    while game.empty_spots():
        if letter == o_player.letter:
            spot = o_player.get_move(game)
        else:
            spot = x_player.get_move(game)

        if game.make_move(spot, letter):
            if print_game:
                print(f'\n{letter} makes a move to the spot {spot}!')
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter

            letter = x_player.letter if letter == o_player.letter else o_player.letter

        else:
            if print_game:
                print('This spot is already taken!')

        time.sleep(1)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    human_player = HumanPlayer('X')
    computer_player = GeniusComputerPlayer('O')
    the_game = TicTacToe()
    play(the_game, human_player, computer_player)