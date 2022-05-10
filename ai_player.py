import player

import threading


class AIPlayer(player.Player):
    def __init__(self, game_logic, position, id_):
        super(AIPlayer, self).__init__(position)
        self.__game_logic = game_logic
        self.__id = id_
        ai_player_input = threading.Thread(target=self.__ai_player_input)
        ai_player_input.start()

    def __ai_player_input(self):
        # ide kell a magic
        # self.__game_logic.handle_input([id_, 'UP' vagy 'DOWN' stb vagy 'BOMB'])
        pass
