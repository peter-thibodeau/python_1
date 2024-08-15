print('COLLATZ SEQUENCE')

# input verification
inp = input('Enter a positive whole number: ')
if inp.isdigit():
    num = int(inp)
else: # a non-numeric character including a dash before a number is an error
    print('Error! enter a positive whole number.')
    quit()

# beginning of output
print('The Collatz Sequence of', num, 'is:')
print(num)

# processing and output of sequence
while(num != 1): # until sequence = 1, don't use num>=1
    if(num %2 == 0):
        num= num // 2
        print(num)
    else:
        num= 3 *num +1
        print(num)
