def square(num):
    return num**2

my_nums = [1,2,3,4,5]

print(map(square,my_nums))

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

# names = ['John','Eve','John']
names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer,names)))

def check_even(num):
    return num % 2 == 0
mynums = [1,2,3,4,5,6]
# output as list
print(list(filter(check_even,mynums)))
# iterat over output
for n in filter(check_even,mynums):
    print(n)
'''
option 01
def square(num):
    result = num ** 2
    return result

option 02
def square(num): return num ** 2
print(square(3))

option 03
def square(num): return num ** 2
print(square(3))
'''
print(list(map(lambda num: num**2,mynums)))

print(list(filter(lambda num:num%2 == 0,mynums)))

print(list(map(lambda name:name[0], names)))

print(list(map(lambda name:name[::-1], names))) # revers names

