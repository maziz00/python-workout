# def display_board():
#     board = [[' ', ' ', ' '],
#              [' ', ' ', ' '],
#              [' ', ' ', ' ']]
    
#     for i in board:
#         for j in i:
#             print(j, end = "  ")
#         print()



# print(display_board(test_board))


# from IPython.display import clear_output

# def display_board(board):

#     for i in board:
#         for j in i:
#             print(j, end = "  ")
#         print()

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# print(display_board(test_board))


from IPython.display import clear_output

def display_board(board):
    # clear_output()
    print(' | |')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |')
    print('------')
    print(' | |')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |')
    print('------')
    print(' | |')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
print(display_board(test_board))