import player
import player_input
import text_ui
import bomb
import game

import random


# Class to handle the game itself.
class GameLogic:
    def __init__(self, number_of_live_players, map_file):
        self.__game_board = self.__load_map(map_file)
        self.__players = self.__create_players(number_of_live_players)
        self.__player_input = player_input.PlayerInput(self, number_of_live_players)
        self.__text_ui = text_ui.TextUI()

        self.__text_ui.update(self.__game_board)
        self.__text_ui.draw()

        self.game = game.Game(self)

    # Function to load a map.
    def __load_map(self, filename):
        game_board = []
        with open(filename, 'r') as map_:
            for line in map_.readlines():
                tmp = []
                for char in line:
                    if char != '\n':
                        tmp.append(char)
                game_board.append(tmp)
        return game_board

    # Function to create the players.
    def __create_players(self, number_of_live_players):
        players = []
        for i in range(number_of_live_players):
            while True:
                position = [random.randint(0, len(self.__game_board) - 1),
                            random.randint(0, len(self.__game_board[0]) - 1)]
                if self.__game_board[position[0]][position[1]] == 'f':
                    break
            player_tmp = player.Player(position)
            players.append(player_tmp)
            # Adding player to the board
            self.__game_board[position[0]][position[1]] = i
        return players

    # Function to get the game board.
    def get_game_board(self):
        return self.__game_board

    # Function to get input from players and call the appropriate methods.
    def handle_input(self, player_input_):
        if player_input_[1] == 'UP' or\
                player_input_[1] == 'DOWN' or\
                player_input_[1] == 'LEFT' or\
                player_input_[1] == 'RIGHT':
            self.__move_player(player_input_[0], player_input_[1])
        elif player_input_[1] == 'BOMB':
            self.__place_bomb(self.__players[player_input_[0]].get_position())

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

            if self.__game_board[future_position[0]][future_position[1]] != 'w' and\
                    self.__game_board[future_position[0]][future_position[1]] != 'e':
                self.__players[player_id].update_position(future_position)
                self.__game_board[current_position[0]][current_position[1]] = 'f'
                self.__game_board[future_position[0]][future_position[1]] = player_id
                self.__text_ui.update(self.__game_board)
                self.__text_ui.draw()
                self.game.build_board()

    # Function to place a bomb.
    def __place_bomb(self, position):
        bomb_ = bomb.Bomb(self, position)

    # Function to detonate a bomb.
    def detonate(self, position):
        print('BOOM')


game_logic = GameLogic(3, './maps/map1.txt')
