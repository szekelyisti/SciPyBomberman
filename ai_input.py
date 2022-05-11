import threading
import random
import time


class AIInput:
    def __init__(self, game_logic, number_of_ai_players):
        if number_of_ai_players != 0:
            self.__input_handler = threading.Thread(target=self.__handle_input, args=(game_logic, number_of_ai_players))
            self.__input_handler.start()
        else:
            pass

    def __handle_input(self, game_logic, number_of_ai_players):
        while True:
            ai_players = game_logic.get_players()[-number_of_ai_players:]
            for player in ai_players:
                if not ((game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] - 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] - 1] == "f" or
                         game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] - 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] - 1] == "w") and
                        (game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] - 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] + 1] == "f" or
                         game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] - 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] + 1] == "w") and
                        (game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] + 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] - 1] == "f" or
                         game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] + 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] - 1] == "w") and
                        (game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] + 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] + 1] == "f" or
                         game_logic.get_game_board()[
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[0] + 1][
                             game_logic.get_players()[game_logic.get_players().index(player)].get_position()[
                                 1] + 1] == "w")):
                    game_logic.handle_input([game_logic.get_players().index(player), 'BOMB'])

                else:
                    num = random.randint(1, 4)

                    if num == 1:
                        game_logic.handle_input([game_logic.get_players().index(player), 'UP'])
                    elif num == 2:
                        game_logic.handle_input([game_logic.get_players().index(player), 'DOWN'])
                    elif num == 3:
                        game_logic.handle_input([game_logic.get_players().index(player), 'LEFT'])
                    else:
                        game_logic.handle_input([game_logic.get_players().index(player), 'RIGHT'])
                time.sleep(1)
