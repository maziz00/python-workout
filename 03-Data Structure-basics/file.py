myfile = open('test.txt')

print(myfile.read())

myfile.seek(0) # to set the curse to begininig of lines

# print(myfile.read())

print(myfile.readlines())

myfilepath = open("/home/maziz/github/code/python-workout/test.txt")

print(myfilepath.read())

myfilepath.seek(0)

print(myfilepath.readlines())


myfile.close()


with open('test.txt') as my_new_file:
    contents = my_new_file.read()

#with open('test.txt', mode='w') as myfile:
#    contents = myfile.read() # io.UnsupportedOperation: not readable

with open('new_test.txt', mode='r') as f:
    print(f.read())

with open('new_test.txt', mode='a') as f:
    print(f.write('\nFOUR ON FOURTH'))

with open('new_test.txt', mode='r') as f:
    print(f.read())


with open('asdfksjhl.txt', mode='w') as f:
    print(f.write('I CREATED THIS FILE!'))

with open('asdfksjhl.txt', mode='r') as f:
    print(f.read())

