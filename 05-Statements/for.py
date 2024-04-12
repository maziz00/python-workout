'''
my_iterable = [1, 2, 3]
for item_name in my_iterable:
  print(item_name)
'''

mylist = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10]
# Numbers
for num in mylist:
    print('Salam')
# Condition with for loop
for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(f'Even Number: {num}')
    else:
        print(f'Odd Number: {num}')
# Sum
list_sum = 0

for num in mylist:
    list_sum = list_sum + num
print(list_sum)
# Strings
for ltr in 'Salam Mohamed':
    print(ltr)
# Variable not requried
for _ in 'Salam Mohamed':
    print("Cool")
# Tuples

tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2), (3,4),(5,6),(7,8)]
print(len(mylist))

for item in mylist:
    print(item)
# Tupe unpacking
for (a,b) in mylist:
    print(a) # first pair of tuple
    print(b) # secon pair of tuple

mylist = [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in mylist:
    print(b)

# Dictionery
d = {'k1': 1, 'k2':2, 'K3':3}
# itera over keys in dictionry
for item in d:
    print(item)

# itera over keys in dictionry
for item in d.items():
    print(item)
# dict unpacking
for value in d.values():
    print(value)






