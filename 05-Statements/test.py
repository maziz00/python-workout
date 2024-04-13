# task 01
st = 'Print only the words that start with s in this sentence Sequence'

for word in st.split():
    # if word[0] == 's':
    # if word[0].lower() == 's': # other solution
      if word[0] == 's' or word[0] == 'S':
        print(word)

# task 02

# print even between 0 - 10
print(list(range(0,11,2)))
# other solution
for num in range(0,11,2):
    print(num)

# task03
# numers devislab by 3
print([x for x in range(1, 51) if x % 3 == 0])

# task04
str = 'Print every word in this sentence that has an even number of letters'

for word in str.split():
    if len(word) % 2 == 0:
        print(word+ ' is even')

# task05

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# task06
ste = 'Print every word in this sentence that has an even number of letters'
print([word[0] for word in ste.split()])