def replacement_choice(game_list, poistion):
    user_placement = input("Type a string to placde at postion: ")

    game_list[poistion] = user_placement

    return game_list