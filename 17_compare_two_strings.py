print('FIND DUPLICATES IN TWO LISTS')

def find_common_elements(a, b, c):
    """ put integers found in a and b into c """
    for i in range(0, len(a)):
        if a[i] in b and a[i] not in c:
            c.append(a[i])
    return c

# get input a and verify it
a = input('Enter a list of integers separated by commas: ')
a = a.split(',')
for i in range(0, len(a)):
    if a[i].isnumeric():
        pass
    else:
        print('Error! enter integers only.')
        quit()

# get input b and verify it
b = input('Enter another list of integers separated by commas: ')
b = b.split(',')
for i in range(0, len(b)):
    if b[i].isnumeric():
        pass
    else:
        print('Error! enter integers only.')
        quit()

c = []

# call the procedure for processing the input
x = find_common_elements(a, b, c)

# print answer
if len(x) == 0:
    print('There are no duplicate integers in the lists.')
else:
    print('The integers found in both lists are: ', ("[{0}]".format(', '.join(map(str, c)))))
