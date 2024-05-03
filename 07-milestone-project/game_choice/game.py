game_on = True
game_list = [0,1,2]

from display_game import display_game
from gameon_choice import gameon_choice
from position_choice import position_choice
from replacement_choice import replacement_choice

while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()
