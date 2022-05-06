class Game:
    def __init__(self, game_id):
        self.player_one_moved = False
        self.player_two_moved = False
        self.ready = False
        self.id = game_id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_moves(self, player):
        return self.moves[player]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.player_one_moved = True
        else:
            self.player_two_moved = True

    def connected(self):
        return self.ready

    def both_moved(self):
        return self.player_two_moved and self.player_one_moved

    def winner(self):
        player_one = self.moves[0].upper()[0]
        player_two = self.moves[1].upper()[0]
        if player_one == 'R' and player_two == 'S':
            winner = 0
        elif player_one == 'S' and player_two == 'R':
            winner = 1
        elif player_one == 'P' and player_two == 'R':
            winner = 0
        elif player_one == 'R' and player_two == 'P':
            winner = 1
        elif player_one == 'S' and player_two == 'P':
            winner = 0
        elif player_one == 'P' and player_two == 'S':
            winner = 1
        else:
            winner = -1
        return winner

    def reset_move(self):
        self.player_one_moved = False
        self.player_two_moved = False
