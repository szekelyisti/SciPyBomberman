import threading
import time


# Class to represent the bomb.
class Bomb:
    def __init__(self, game_logic, position):
        self.__position = position
        self.__timer = threading.Thread(target=self.__timer, args=(game_logic,))
        self.__timer.start()

    # Function to detonate bomb after some time.
    def __timer(self, game_logic):
        time.sleep(3)
        game_logic.detonate(self.__position)
