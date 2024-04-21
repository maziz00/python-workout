x =25

def printer():
    x = 50
    return x

print(x) # 25
print(printer()) # 50
'''
LEGB
L: Local - names assigned in any way within a function (def or lambda) and not declared global in that function
E: Enclosing function locals - name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
G: Global (module) - name assigned at the top-level of a module file, or declared global in a def within the file.
B: Built-in (Python) - names preassigned in the built-in names module: open, range, SyntaxError,...
'''

# lambda num:num**2

# Global
name = 'This Is Global String'

def greet():
    # Enclosing
    name = 'Mohamed'

    def salam():
        # Local
        name = 'Iam A Local'
        print('Salam ' + name)

    salam()

greet()

x = 50

def func(x):
    print(f'X is {x}')
    # Local Reassignment!
    x = 200
    print(f'I Just Locally Changed X To {x}')

print(func(x))
print(x)


x = 70

def func1():
    global x
    print(f'X is {x}')
    # Local Reassignment!
    x = 'New Value'
    print(f'I Just Global Changed X To {x}')

print(func1())
print(x)


x = 70

def func2(x):
    print(f'X is {x}')
    # Local Reassignment!
    x = 'New Value'
    print(f'I Locally X To {x}')
    return x

print(func2(x))
print(x)