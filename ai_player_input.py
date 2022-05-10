import threading

class AIPlayerInput:

    def __init__(self, game_logic, number_of_live_players):
        self.__input_handler = threading.Thread(target=self.__handle_input, args=(game_logic, number_of_live_players))
        self.__input_handler.start()

    def __handle_input(self):


