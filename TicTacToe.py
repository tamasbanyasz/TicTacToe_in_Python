import numpy as np


class Map:
    def __init__(self):
        self.rows = 3   # number of rows
        self.cols = 3   # number of columns
        self.board = np.array([['-'] * self.cols] * self.rows)

    def display_map(self):  # display the map
        for i in self.board:
            for j in i:
                print(j, end=' ')
            print()

    def valid_rows_n_cols(self, row_n_col, sign):
        if self.board[row_n_col[0] - 1, row_n_col[1] - 1] == '-':  # if player hit is on '-' mark
            self.board[row_n_col[0] - 1, row_n_col[1] - 1] = sign  # turn the mark to player sign
        elif self.board[row_n_col[0] - 1, row_n_col[1] - 1] != '-':
            return False

        return True


class Player:
    def __init__(self, signs):
        self.sign = signs  # ['X', 'O']

    def player_number(self, count):
        number_1 = int(input(f"Your turn {self.sign[count]}. Row: "))
        number_2 = int(input(f"Your turn {self.sign[count]}. Col: "))

        return [number_1, number_2]

    def player_sign(self, count):
        return self.sign[count]


class TicTacToe:
    def __init__(self, signs):
        self.signs = signs
        self.map = Map()
        self.plyr = Player(self.signs)
        self.count = 0

    def player_win(self, sign):
        idx = [i for i in range(len(self.map.board))]

        index = 0
        while index <= len(idx) - 1:
            rows = np.all(self.map.board[index, :] == sign)  # if all rows equals a player sign
            cols = np.all(self.map.board[:, index] == sign)  # if all columns equals a player sign

            diag1 = np.all(self.map.board[idx, idx] == sign)  # if all diagonal equals a player sign
            diag2 = np.all(self.map.board[idx[::-1], idx] == sign)

            index += 1

            if np.any([rows, cols, diag1, diag2]):  # return True if player filled any line
                return True

        return False

    def player_turn(self):  # count the turns
        if self.count < len(self.signs) - 1:
            self.count += 1
        else:
            self.count = 0

    def game_draw(self):  # draw if no more '-' mark
        for i in self.map.board:
            if '-' in i:
                return False

        return True

    def game(self):

        while True:

            self.map.display_map()

            if self.game_draw():
                print('DRAW!')
                break

            if not self.map.valid_rows_n_cols(self.plyr.player_number(self.count), self.plyr.player_sign(self.count)):  # if player hit the other player sign
                print("WRONG!")
                self.count -= 1

            if self.player_win(self.plyr.player_sign(self.count)):
                self.map.display_map()
                print(f'Player {self.plyr.player_sign(self.count)} WON!')
                break

            self.player_turn()


tic_tac_toe = TicTacToe(['X', 'O'])

if __name__ == "__main__":
    tic_tac_toe.game()
    
