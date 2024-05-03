def display_board():
    board = [[' 1', ' ', ' 3'],
             [' ', ' 5', ' '],
             [' 7', ' ', ' 9']]
    
    for i in board:
        for j in i:
            print(j, end = "  ")
        print()


print(display_board())