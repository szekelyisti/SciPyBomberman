import player
import random
import threading


class AIPlayer(player.Player):

    def __init__(self, game_logic, position, id_):
        self.__position = position
        self.__game_logic = game_logic
        self.__id = id_
        ai_player_input = threading.Thread(target=self.__ai_player_input)
        ai_player_input.start()

    def __ai_player_input(self):
        # ide kell a magic
        if not ((self.__game_logic.get_game_board()[self.__position[0] - 1][self.__position[1] - 1] == "f" or
                 self.__game_logic.get_game_board()[self.__position[0] - 1][self.__position[1] - 1] == "w") and
                (self.__game_logic.get_game_board()[self.__position[0] - 1][self.__position[1] + 1] == "f" or
                 self.__game_logic.get_game_board()[self.__position[0] - 1][self.__position[1] + 1] == "w") and
                (self.__game_logic.get_game_board()[self.__position[0] + 1][self.__position[1] - 1] == "f" or
                 self.__game_logic.get_game_board()[self.__position[0] + 1][self.__position[1] - 1] == "w") and
                (self.__game_logic.get_game_board()[self.__position[0] + 1][self.__position[1] + 1] == "f" or
                 self.__game_logic.get_game_board()[self.__position[0] + 1][self.__position[1] + 1] == "w")):
            self.__game_logic.handle_input([self.__id, 'BOMB'])

        else:
            num = random.randint(1, 4)

            if num == 1:
                self.__game_logic.handle_input([self.__id, 'UP'])
            elif num == 2:
                self.__game_logic.handle_input([self.__id, 'DOWN'])
            elif num == 3:
                self.__game_logic.handle_input([self.__id, 'LEFT'])
            else:
                self.__game_logic.handle_input([self.__id, 'RIGHT'])
