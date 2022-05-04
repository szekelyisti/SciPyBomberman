import player_input
import game_logic


_game_logic = game_logic.GameLogic(2, 20, 10)
player1 = player_input.PlayerInput(_game_logic, "first")
