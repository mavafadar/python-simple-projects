class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print('-' * 13)
            print('| ' + ' | '.join(row) + ' |')
        print('-' * 13)

    def available_moves(self):
        moves = list()
        for i, row in enumerate(self.board):
            for j, spot in enumerate(row):
                if spot == ' ':
                    moves.append((i, j))
        return moves

    def empty_spots(self):
        for row in self.board:
            if ' ' in row:
                return True
        return False

    def number_of_empty_spots(self):
        return len(self.available_moves())

    def make_move(self, spot, letter):
        row, column = spot[0], spot[1]
        if self.board[row][column] == ' ':
            self.board[row][column] = letter
            if self.winner(letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, letter):
        transposed_board = list(map(list, zip(*self.board)))
        for i in range(3):
            if self.board[i].count(letter) == 3 or transposed_board[i].count(letter) == 3:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == letter:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == letter:
            return True
        return False
