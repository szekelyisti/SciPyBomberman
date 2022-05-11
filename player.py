# Class to represent a player.
class Player:

    __previous_step = None

    def __init__(self, position, real):
        self.__position = position
        self.__lives = 3
        self.__real = real
        self.__alive = True

    # Function to get the position of the player.
    def get_position(self):
        return self.__position

    # Function to set a new position of the player.
    def update_position(self, position):
        self.__position = position

    def set_previous_step(self, step):
        self.__previous_step = step

    def get_previous_step(self):
        return self.__previous_step

    def is_alive(self):
        return self.__alive

    def kill(self):
        self.__alive = False

    def hp_loss(self):
        self.__lives = self.__lives = 1
        if self.__lives == 0:
            self.kill()
