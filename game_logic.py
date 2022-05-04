import random


# Class to handle the game itself.
class GameLogic:
    def __init__(self, player_num, size_x, size_y):
        self.__board = self.generate_board(player_num, size_x, size_y)
        self.test_print(self.__board)

    # Function to get input from players and call the appropriate methods.
    def push_input(self, _input):
        if _input[1] == ('up' or 'down' or 'left' or 'right'):
            self.move_player(_input[0], _input[1])

    # Function to generate the game board.
    def generate_board(self, player_num, size_x, size_y):
        board = []
        for i in range(size_y):
            tmp = []
            for j in range(size_x):
                tmp.append(' ')
            board.append(tmp)
        for i in range(size_x * size_y // 2):  # todo: implement generate algorithm
            board[random.randint(0, size_y - 1)][random.randint(0, size_x - 1)] = 'X'
        for i in range(1, player_num + 1):
            board[random.randint(0, size_y - 1)][random.randint(0, size_x - 1)] = i
        return board

    def move_player(self, player, direction):
        print(player + ' - ' + direction)

    def test_print(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end='')
            print()




