import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            choice = input(f'\n{self.letter}\'s turn. Enter row then column with space in between: ')
            try:
                choice = choice.split()
                if len(choice) != 2:
                    print('Not a valid input.')
                    continue
                row = int(choice[0])
                column = int(choice[1])
            except ValueError or IndexError:
                print('Not a valid input.')
                continue
            if not (0 <= row <= 2 and 0 <= column <= 2):
                print('Not a valid input.')
                continue
            return row, column


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    @staticmethod
    def find_other_player(state, player):
        flatten_board = [item for row in state.board for item in row]
        flatten_filtered_board = [item for item in flatten_board if item != player and item != ' ']
        return flatten_filtered_board[0]

    def minimax(self, state, player):
        max_player = self.letter
        other_player = self.find_other_player(state, player)

        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.number_of_empty_spots() + 1) if other_player == max_player else -1 * (
                            state.number_of_empty_spots() + 1)
            }
        elif not state.empty_spots():
            return {
                'position': None,
                'score': 0
            }

        if player == max_player:
            best = {
                'position': None,
                'score': -math.inf
            }
        else:
            best = {
                'position': None,
                'score': math.inf
            }

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            simulated_score = self.minimax(state, other_player)
            state.board[possible_move[0]][possible_move[1]] = ' '
            state.current_winner = None
            simulated_score['position'] = possible_move
            if player == max_player:
                if simulated_score['score'] > best['score']:
                    best = simulated_score
            else:
                if simulated_score['score'] < best['score']:
                    best = simulated_score

        return best

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return 0, 0
        return self.minimax(game, self.letter)['position']
