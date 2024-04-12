mylist = [1, 2, 3, 4, 5]
for num in range(10):
    print(num)

for num1 in range(0,11,2):
    print(num1)

# Genrator
print(list(range(0,11,2)))

index_count = 0

for ltr in 'abcd':
    print('At index {} the letter is {}'.format(index_count,ltr))
    index_count += 1

word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3,4,5]
mylist2 = ['a', 'b', 'c']
mylist3 = [100,200,300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2, mylist3)))

for a,b,c in zip(mylist1, mylist2, mylist3):
    print(b)

print('x' in [1,2,3])

print(2 in [1,2,3])

print('a' in 'a world')

print( 'k1' in {'k1': 445})
d = {'k1': 445}

print(445 in d.keys)
print(445 in d.values)