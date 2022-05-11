import game_logic


# Script to start things.
number_of_live_players = 2
number_of_ai_players = 0
map_file = './maps/map1.txt'

game_logic = game_logic.GameLogic(number_of_live_players, number_of_ai_players, map_file)
