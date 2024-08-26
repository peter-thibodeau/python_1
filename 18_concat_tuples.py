print('CONCATENATE TWO TUPLES')

def concat_tuples(a,b):
    """ concatenate tuples a and b """
    return a + b

# obtain input and convert to tuple
a = input('Enter numbers, letters, phrases, etc. separated by commas for first tuple: ')
a = a.split(',')
a = tuple(a)

# obtain input and convert to tuple
b = input('Enter numbers, letters, phrases, etc. separated by commas for second tuple: ')
b = b.split(',')
b = tuple(b)

# call function to process inputs
x = concat_tuples(a,b)

# output
print(x)
