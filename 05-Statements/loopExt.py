x = [1,2,3]
# Pass
for item in x:
    # comment
    pass # remove syntax error
print('end of my script')
# Continue
mystring = "Mohamed"

for ltr in mystring:
    if ltr == 'a':
        continue
    print(ltr)
# Break
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
