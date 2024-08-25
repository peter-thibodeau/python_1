print('FIND DUPLICATES IN TWO LISTS')

# get input
a = input('Enter a list of integers separated by commas: ')
b = input('Enter another list of integers that is the same length as a, separated by commas: ')
c = []

# convert input to lists
a = a.split(',')
b = b.split(',')

def find_common_elements(a, b, c):
    """ put integers found in a and b into c """
    for i in range(0, len(a)):
        if a[i] in b and a[i] not in c:
            c.append(a[i])
    return c

# call the procedure for processing the input
x = find_common_elements(a, b, c)

# print answer
if len(x) > 0:
    print('The integers found in both lists are: ', x)
else:
    print('There are no duplicate integers in the lists.')
