mystr = 'Salam Mohamed'

mylist = []
# calssic way of list comperhension
for ltr in mystr:
    mylist.append(ltr)

print(mylist)

m1list = [ltr for ltr in mystr] # flaten for loop here

print(m1list)

m2list = [x for x in 'word']
print(m2list)


m3list = [num for num in range(0,11)]

print(m3list)

m4list = [num**2 for num in range(0,11)]

print(m4list)

m5list = [x for x in range(0,11) if x%2 == 0]

print(m5list)

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)* temp + 32) for temp in celcius]
print(fahrenheit)

# another way
f1 = []
for temp in celcius:
    f1.append((9/5)* temp + 32)
print(f1)

results = [x if x %2 == 0 else 'ODD' for x in range(0,11)]
print(results)

m6list = []

for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        m6list.append(x*y)

print(m6list)

m7list = [x*y for x in [2, 4, 6] for y in [1,10,1000]]

print(m7list)