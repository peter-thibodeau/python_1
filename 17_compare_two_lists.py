print('COMPARE TWO LISTS')

# get the lists
a = input('Enter a list of integers separated by commas: ')
b = input('Enter another list with the same amount of integers separated by commas: ')
c = []


# verify lists contain integers only
if a.isnumeric() and b.isnumeric():
    # convert a to integer
    for i in range(0, len(a)):
        a[i] = int(a[i])
    # convert b to integer
    for i in range(0, len(b)):
        b[i] = int(b[i])
else:
    print('Error! the lists must contain integers only.')
    quit()

print(len(a))
print(a)