import threading
import random
import time


class AIInput:
    def __init__(self, game_logic, number_of_ai_players):
        if number_of_ai_players != 0:
            self.__input_handler = threading.Thread(target=self.__handle_input, args=(game_logic, number_of_ai_players))
            self.__input_handler.start()
            print("gogogo")
        else:
            pass

    def __handle_input(self, game_logic, number_of_ai_players):
        while True:
            ai_players = game_logic.get_players()[-number_of_ai_players:]
            for player in ai_players:
                free_neighbors = []
                if player.get_previous_step() != "BOMB":
                    free_neighbors.append("BOMB")

                if game_logic.get_game_board()[player.get_position()[0] - 1][player.get_position()[1]] == "f" and player.get_previous_step() != "DOWN":
                    free_neighbors.append("UP")
                    free_neighbors.append("UP")
                    free_neighbors.append("UP")
                if game_logic.get_game_board()[player.get_position()[0] + 1][player.get_position()[1]] == "f" and player.get_previous_step() != "UP":
                    free_neighbors.append("DOWN")
                    free_neighbors.append("DOWN")
                    free_neighbors.append("DOWN")
                if game_logic.get_game_board()[player.get_position()[0]][player.get_position()[1] - 1] == "f" and player.get_previous_step() != "RIGHT":
                    free_neighbors.append("LEFT")
                    free_neighbors.append("LEFT")
                    free_neighbors.append("LEFT")
                if game_logic.get_game_board()[player.get_position()[0]][player.get_position()[1] + 1] == "f" and player.get_previous_step() != "LEFT":
                    free_neighbors.append("RIGHT")
                    free_neighbors.append("RIGHT")
                    free_neighbors.append("RIGHT")

                if len(free_neighbors) == 0:
                    if player.get_previous_step() == "LEFT":
                        free_neighbors.append("RIGHT")
                    elif player.get_previous_step() == "RIGHT":
                        free_neighbors.append("LEFT")
                    elif player.get_previous_step() == "UP":
                        free_neighbors.append("DOWN")
                    elif player.get_previous_step() == "DOWN":
                        free_neighbors.append("UP")
                    else:
                        free_neighbors.append("UP")
                        free_neighbors.append("DOWN")
                        free_neighbors.append("LEFT")
                        free_neighbors.append("RIGHT")

                step = random.randint(0, len(free_neighbors)-1)
                game_logic.handle_input([game_logic.get_players().index(player), free_neighbors[step]])
                player.set_previous_step(free_neighbors[step])

                time.sleep(1)
