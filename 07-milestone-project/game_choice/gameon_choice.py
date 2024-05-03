def gameon_choice():
    choice = 'Wrong'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choos Y or N ")

        if choice == "Y":
            return True
        else:
            return False