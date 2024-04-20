def myfunc(a,b):
    # Return 5% of the sume of a and b
    return sum((a,b)) * 0.05

print(myfunc(40,60))

def myfunc1(a,b,c=0,d=0,e=0):
    return sum((a,b,c,d,e)) * 0.05

print(myfunc1(40,60,100,100,4))

def myfunc2(*args):
    return sum(args) * 0.05 # add as many arguments as we want to the function as tuple

print(myfunc2(40,60,100,10,4,5,10))

def myfunc3(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is: {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc3(fruit = 'apple', veggie = 'lettuce')

def myfunc4(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc4(10,20,30, fruit = 'orange', food = 'eggs', animal = 'tiger')