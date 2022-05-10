import player

import threading


class AIPlayer(player.Player):
    def __init__(self, id_, position):
        super(AIPlayer, self).__init__(id_, position)
        ai_player_input = threading.Thread(target=self.__ai_player_input, args=(id_,))
        ai_player_input.start()

    def __ai_player_input(self, id_):
        # ide kell a magic
        pass
