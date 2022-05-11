import threading
from pynput import keyboard


# Class to handle keyboard inputs from a player.
class PlayerInput:

    __over = False

    def __init__(self, game_logic, number_of_live_players):
        self.__input_handler = threading.Thread(target=self.__handle_input, args=(game_logic, number_of_live_players))
        self.__input_handler.start()

    # Function to handle keyboard inputs from a player.
    #test
    def __handle_input(self, game_logic, number_of_live_players):
        while True:
            with keyboard.Events() as events:
                event = events.get()

                if number_of_live_players >= 1:
                    if game_logic.get_players()[0].is_alive():
                        if str(event) == 'Press(key=Key.up)':
                            game_logic.handle_input([0, 'UP'])
                        elif str(event) == 'Press(key=Key.down)':
                            game_logic.handle_input([0, 'DOWN'])
                        elif str(event) == 'Press(key=Key.left)':
                            game_logic.handle_input([0, 'LEFT'])
                        elif str(event) == 'Press(key=Key.right)':
                            game_logic.handle_input([0, 'RIGHT'])
                        elif str(event) == 'Press(key=Key.enter)':
                            game_logic.handle_input([0, 'BOMB'])

                if number_of_live_players >= 2:
                    if game_logic.get_players()[1].is_alive():
                        if str(event) == "Press(key='w')":
                            game_logic.handle_input([1, 'UP'])
                        elif str(event) == "Press(key='s')":
                            game_logic.handle_input([1, 'DOWN'])
                        elif str(event) == "Press(key='a')":
                            game_logic.handle_input([1, 'LEFT'])
                        elif str(event) == "Press(key='d')":
                            game_logic.handle_input([1, 'RIGHT'])
                        elif str(event) == 'Press(key=Key.space)':
                            game_logic.handle_input([1, 'BOMB'])
            if self.__over:
                break

    def game_over_fun(self):
        self.__over = True
        self.__input_handler.join()
        print("real stopped")