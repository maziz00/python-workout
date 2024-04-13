'''
def name_of_function():

print("Salam")

name_of_function(Mohamed)
Salam Mohamed
'''

def add_func(num1, num2):
    return num1 + num2 # return all to save the function resutls in variable

result = add_func(2, 4)
print(result)


def say_salam():
    print("Salam")
    print("are")
    print("You")
    print("OK")


def say_salam(name='kamal'):
    print(f'Salam {name}')

say_salam("Mohamed")

def print_result(a,b):
    print(a,b)

def return_result(a,b):
    return a + b

print_result(10, 20)

r_print = print_result(10,20)

print(r_print, type(r_print))

return_result(10,20)

result = return_result(10,20)

print(result)

# not always used print and return in one function
def myfunc(a,b):
    print(a+b) # to print result only
    return a+b # to save result in variable

# python is dynamicly type programming language
def sum_numbers(num1, num2):
    return num1 + num2
# bug as input types not correct
print(sum_numbers('20','30'))