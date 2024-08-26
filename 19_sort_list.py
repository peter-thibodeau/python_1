print('SORT A LIST')

# get input a and convert it to a list
a = input('Enter a list of integers separated by commas: ')
a = a.split(',')

def sort_list(a):
    """ sort list a """
    a.sort(key=int)
    return a

# verify that list a contains only integers
for i in range(0, len(a)):
    if a[i].isnumeric():
        pass
    else:
        print('Error! enter only integers.')
        quit()

# call function to sort list a
x = sort_list(a)

# output
print(x)
