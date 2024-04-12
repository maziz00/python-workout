t = (1, 2, 3)
mylist = [1, 2, 3]

print(type(t), type(mylist))


print(len(t))

t = ('one', 2)

print(t)

t = (1, 2, 3)

print(t[0], t[-1])

t = ('a', 'a', 'b', 'a')

print(t.count('a'))
print(t.index('a'))
print(t.index('b'))

mylist[0]= 'New'

t[0] = 'New' # TypeError: 'tuple' object does not support item assignment

print(t)