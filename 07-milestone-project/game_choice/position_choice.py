def position_choice():
    choice = 'Wrong'

    while choice not in ['0', '1', '2']:

        choice = input("Pick a postion (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice!")

    return int(choice)