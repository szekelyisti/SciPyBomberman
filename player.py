# Class to represent a player.
class Player:
    def __init__(self, id_, position):
        self.__id_ = id_
        self.__position = position
        self.__lives = 3

    # Function to decrement lives. Returns 'True' if no lives is remaining.
    def die(self):
        self.__lives -= 1
        if self.__lives == 0:
            return True

    # Function to get the position of the player.
    def get_position(self):
        return self.__position

    # Function to set a new position of the player.
    def update_position(self, position):
        self.__position = position
