example = [1,2,3,4,5,6,7]
from random import shuffle
print(shuffle(example)) # return nothing shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

mylist = [' ',' ','O',' ',' ']

print(shuffle_list(mylist))

def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2 ")

    return int(guess)

print(player_guess())


def check_guss(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)

# INITIAL LISt
mylist = [' ', 'O', ' ']

# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

# USER GUSS
guess = player_guess()

# CHECK GUESS
check_guss(mixedup_list, guess)