my_dict = {'key1': 'value1', 'key2':'value2'}

print(my_dict['key1'])

prices_lookup = { 'apple': 2.99, 'oranges': 2.10, 'milk': 6.2}

print(prices_lookup['apple'])


d = {'k1': 123, 'k2': [0,1,2], 'k3':{'insidekey':100}}

print(d['k2'][2])

print(d['k3']['insidekey'])


d = { 'key1': ['a', 'b', 'c']}

mylist = d['key1']
letter = mylist[2]
print(letter.upper())

# short way
print(d['key1'][1].upper())


d = {'k1': 100, 'k2': 200}
d['k3'] = 300

print(d)

d['k1'] = 'NEW VALUE'
print(d)

d = {'k1': 100,'k2': 200, 'k3': 300}


print(d.keys())
print(d.values())
print(d.items())

