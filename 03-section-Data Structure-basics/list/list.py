my_list = [1, 2, 3]

my_list = ['one', 'two', 'three']

another_list = ['four', 'five', 'six']

new_list = my_list + another_list

print(len(my_list))
print(my_list[0])
print(my_list[1:])

print(my_list + another_list)

new_list[0] = 'ONE ALL CAPS'

print(new_list)

new_list.append('seven')

print(new_list)

print(new_list.pop())

print(new_list)

popped_item = new_list.pop()

print(popped_item)

print(new_list.pop(0))

print(new_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1 , 8, 3]


new_list.sort()
print(new_list)

my_sorted_list = new_list.sort() # wrong assgine sort will return nothing
print(type(my_sorted_list))

# the correct way of sort
new_list.sort()
my_sorted_list = new_list
print(my_sorted_list)

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)