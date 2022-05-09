import player
import player_input
import text_ui

import random


# Class to handle the game itself.
class GameLogic:
    def __init__(self, number_of_players, lives, size):
        self.__players = self.__create_players(number_of_players, lives)
        self.__game_board = self.__generate_game_board(number_of_players, size)
        self.__player_input = player_input.PlayerInput(self)
        self.__text_ui = text_ui.TextUI()

        self.__text_ui.update(self.__game_board)
        self.__text_ui.draw()

    # Function to create the players.
    def __create_players(self, number_of_players, lives):
        players = []
        for i in range(number_of_players):
            player_tmp = player.Player(lives)
            players.append(player_tmp)
        return players

    # Function to generate the game board.
    def __generate_game_board(self, number_of_players, size):
        # Generating a 'clear' board of given size.
        game_board = []
        for i in range(size[1]):
            tmp = []
            for j in range(size[0]):
                tmp.append(' ')
            game_board.append(tmp)
        # Generating walls.
        for i in range(size[0] * size[1] // 2):  # todo: implement generate algorithm
            game_board[random.randint(0, size[1] - 1)][random.randint(0, size[0] - 1)] = 'X'
        # Adding player(s).
        for i in range(number_of_players):
            position = [random.randint(0, size[1] - 1), random.randint(0, size[0] - 1)]
            game_board[position[0]][position[1]] = i
            # Set the starting position of player(s).
            self.__players[i].update_position(position)
        return game_board

    # Function to get input from players and call the appropriate methods.
    def handle_input(self, player_input):
        if player_input[1] == 'UP' or 'DOWN' or 'LEFT' or 'RIGHT':
            self.__move_player(player_input[0], player_input[1])

    # Function to move the player if possible.
    def __move_player(self, player_id, direction):
        current_position = self.__players[player_id].get_position()
        future_position = current_position.copy()

        if direction == 'UP':
            future_position[0] -= 1
        elif direction == 'DOWN':
            future_position[0] += 1
        elif direction == 'LEFT':
            future_position[1] -= 1
        elif direction == 'RIGHT':
            future_position[1] += 1

        if 0 <= future_position[0] < len(self.__game_board[0]) and\
                0 <= future_position[1] < len(self.__game_board[1]):
            if self.__game_board[future_position[0]][future_position[1]] != 'X':
                self.__players[player_id].update_position(future_position)
                self.__game_board[current_position[0]][current_position[1]] = ' '
                self.__game_board[future_position[0]][future_position[1]] = player_id
                self.__text_ui.update(self.__game_board)
                self.__text_ui.draw()
