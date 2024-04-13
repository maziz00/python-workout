def even_check(number):
    return number % 2 == 0

print(even_check(11))

def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            # print(f"{num} is even")
            return True
        else:
            # print(f"{num} is odd")
            # return False # WRONGE!!!
            pass
    return False

print(check_even_list([1,2,4,5]))

def check_even_list_v1(num_list):
    # returna all the even number in a list

    # place holder vaiables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print(check_even_list_v1([1,2,3,4,5]))