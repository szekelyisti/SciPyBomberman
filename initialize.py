import game_logic


# Script to start things.
number_of_players = 2
lives = 3
map_file = './maps/map1.txt'

game_logic = game_logic.GameLogic(number_of_players, lives, map_file)
