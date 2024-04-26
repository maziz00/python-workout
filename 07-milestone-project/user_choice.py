def user_choice():
    # VARIABLES

    # Initial
    choice = 'WRONG'
    acceptable_range = range(1,11)
    within_range = False

    # TWO CONDITIONS TO CHECK
    # 1. IS THE INPUT AN DIGIT?
    # 2. IS THE INPUT WITHIN THE RANGE?

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (1-10): ")

        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print("You have entered {} which is within the range".format(choice))
            else:
                print("Sorry that is not within the range!")
                within_range = False

    return int(choice)

if __name__ == "__main__":
    user_choice()