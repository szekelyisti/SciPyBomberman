import threading

import player
import player_input
import ai_input
import text_ui
import bomb

import random
import time


# Class to handle the game itself.
class GameLogic:
    def __init__(self, number_of_live_players, number_of_ai_players, map_file):
        self.__live_players_num = number_of_live_players
        self.__ai_players_num = number_of_ai_players

        self.__game_board = self.__load_map(map_file)
        self.__players = self.__create_players(number_of_live_players, number_of_ai_players)
        self.__live_player_input = player_input.PlayerInput(self, number_of_live_players)
        self.__ai_player_input = ai_input.AIInput(self, number_of_ai_players)

        threading.Thread(target=self.__text_ui).start()

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
    def __create_players(self, number_of_live_players, number_of_ai_players):
        players = []
        # Create live players.
        for i in range(number_of_live_players):
            while True:
                position = [random.randint(0, len(self.__game_board) - 1),
                            random.randint(0, len(self.__game_board[0]) - 1)]
                if self.__game_board[position[0]][position[1]] == 'f':
                    break
            player_tmp = player.Player(position, True)
            players.append(player_tmp)
            # Adding player to the board
            self.__game_board[position[0]][position[1]] = i
        # Create AI players.
        id_ = number_of_live_players
        for i in range(number_of_ai_players):
            while True:
                position = [random.randint(0, len(self.__game_board) - 1),
                            random.randint(0, len(self.__game_board[0]) - 1)]
                if self.__game_board[position[0]][position[1]] == 'f':
                    break
            player_tmp = player.Player(position, False)
            players.append(player_tmp)
            # Adding player to the board
            self.__game_board[position[0]][position[1]] = id_
            id_ += 1
        return players

    def __text_ui(self):
        while(True):
            text_ui_ = text_ui.TextUI()
            text_ui_.update(self.__game_board)
            text_ui_.draw()
            time.sleep(1)

    def get_players(self):

        return self.__players

    def get_live_players_num(self):
        return self.__live_players_num

    def get_ai_players_num(self):
        return self.__ai_players_num

    # Function to get the game board.
    def get_game_board(self):
        return self.__game_board

    # Function to get input from players and call the appropriate methods.
    def handle_input(self, player_input_):
        if player_input_[1] == 'UP' or \
                player_input_[1] == 'DOWN' or \
                player_input_[1] == 'LEFT' or \
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

        if str(self.__game_board[current_position[0]][current_position[1]]).isdigit():
            if self.__game_board[future_position[0]][future_position[1]] == 'f':
                self.__game_board[future_position[0]][future_position[1]] = player_id
                self.__game_board[current_position[0]][current_position[1]] = 'f'
                self.__players[player_id].update_position(future_position)
            elif self.__game_board[future_position[0]][future_position[1]] == 'b':
                self.__game_board[future_position[0]][future_position[1]] = str(player_id) + 'b'
                self.__game_board[current_position[0]][current_position[1]] = 'f'
                self.__players[player_id].update_position(future_position)
            elif self.__game_board[future_position[0]][future_position[1]] == 'q':
                self.__game_board[future_position[0]][future_position[1]] = str(player_id) + 'q'
                self.__game_board[current_position[0]][current_position[1]] = 'f'
                self.__players[player_id].update_position(future_position)
        elif str(self.__game_board[current_position[0]][current_position[1]])[1] == 'b':
            if self.__game_board[future_position[0]][future_position[1]] == 'f':
                self.__game_board[future_position[0]][future_position[1]] = player_id
                self.__game_board[current_position[0]][current_position[1]] = 'b'
                self.__players[player_id].update_position(future_position)
            elif self.__game_board[future_position[0]][future_position[1]] == 'b':
                self.__game_board[future_position[0]][future_position[1]] = str(player_id) + 'b'
                self.__game_board[current_position[0]][current_position[1]] = 'b'
                self.__players[player_id].update_position(future_position)
            elif self.__game_board[future_position[0]][future_position[1]] == 'q':
                self.__game_board[future_position[0]][future_position[1]] = str(player_id) + 'q'
                self.__game_board[current_position[0]][current_position[1]] = 'b'
                self.__players[player_id].update_position(future_position)
        elif str(self.__game_board[current_position[0]][current_position[1]])[1] == 'q':
            if self.__game_board[future_position[0]][future_position[1]] == 'f':
                self.__game_board[future_position[0]][future_position[1]] = player_id
                self.__game_board[current_position[0]][current_position[1]] = 'q'
                self.__players[player_id].update_position(future_position)
            elif self.__game_board[future_position[0]][future_position[1]] == 'b':
                self.__game_board[future_position[0]][future_position[1]] = str(player_id) + 'b'
                self.__game_board[current_position[0]][current_position[1]] = 'q'
                self.__players[player_id].update_position(future_position)
            elif self.__game_board[future_position[0]][future_position[1]] == 'q':
                self.__game_board[future_position[0]][future_position[1]] = str(player_id) + 'q'
                self.__game_board[current_position[0]][current_position[1]] = 'q'
                self.__players[player_id].update_position(future_position)

    # Function to place a bomb.
    def __place_bomb(self, position):
        if str(self.__game_board[position[0]][position[1]])[-1]\
                != 'b':
            bomb_ = bomb.Bomb(self, position)
            self.__game_board[position[0]][position[1]] = str(self.__game_board[position[0]][position[1]]) + 'b'

    # Function to detonate a bomb.
    def detonate(self, position):
        print('boom')

        if self.__game_board[position[0]][position[1]] == 'b':
            self.__game_board[position[0]][position[1]] = 'q'
        else:
            self.__game_board[position[0]][position[1]] = str(self.__game_board[position[0]][position[1]])[0] + 'q'
            # todo: call die










        '''indexes = [[position[0],     position[1]],
                   [position[0] - 1, position[1]],
                   [position[0] - 2, position[1]],
                   [position[0],     position[1] + 1],
                   [position[0],     position[1] + 2],
                   [position[0] + 1, position[1]],
                   [position[0] + 2, position[1]],
                   [position[0],     position[1] - 1],
                   [position[0],     position[1] - 2]]

        for index in indexes:
            if self.__game_board[index[0]][index[1]] == 'b' or \
                    self.__game_board[index[0]][index[1]] == 'q' or \
                    self.__game_board[index[0]][index[1]] == 'f' or \
                    self.__game_board[index[0]][index[1]] == 'e':
                self.__game_board[index[0]][index[1]] = 'q'






        if self.__game_board[position[0]][position[1]] == 'e':
            self.__game_board[position[0]][position[1]] = 'q'
        elif self.__game_board[position[0]][position[1]] == 'f':
            self.__game_board[position[0]][position[1]] = 'q'
            if self.__game_board[position[0]][position[2]] == 'f':
                self.__game_board[position[0]][position[2]] = 'q'
            elif self.__game_board[position[0]][position[2]].isnumeric():
                self.__players[int(self.__game_board[position[0]][position[2]])].die()





        print('test')
        print(self.__game_board[position[0]][position[1]])'''
