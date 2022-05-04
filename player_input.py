import threading
from pynput import keyboard


# Class to handle keyboard inputs from a player.
class PlayerInput:
    def __init__(self, _game_logic, player):
        input_handler = threading.Thread(target=self.handle_input, args=(_game_logic, player,))
        input_handler.start()

    # Function to handle keyboard inputs from a player.
    def handle_input(self, _game_logic, player):
        while True:
            with keyboard.Events() as events:
                event = events.get()
                if str(event.key) == 'Key.up':
                    _game_logic.push_input([player, 'up'])
                elif str(event.key) == 'Key.down':
                    _game_logic.push_input([player, 'down'])
                elif str(event.key) == 'Key.left':
                    _game_logic.push_input([player, 'left'])
                elif str(event.key) == 'Key.right':
                    _game_logic.push_input([player, 'right'])
