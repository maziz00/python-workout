def player_input():
    marker = ''
    # Keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choos X or O: ').upper()

    # Assign player 2 the opposite marker
    player1 = marker

    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    
print(player_input())