# Class for text ui.
class TextUI:
    def __init__(self):
        self.__game_board = None

    # Function to update the contents.
    def update(self, game_board):
        self.__game_board = game_board

    # Function to draw the contents.
    def draw(self):
        for i in range(len(self.__game_board)):
            for j in range(len(self.__game_board[0])):
                print(self.__game_board[i][j], end='')
            print()
        print()
