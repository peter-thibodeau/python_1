print('IS IT A PRIME NUMBER?')
import math

def is_prime(num):
    """ determine if numut is a prime number """
    for i in range(2, int(math.sqrt(num))+1):
        if (num%i) == 0:
          return None
    return True

# get input, verify it, and call function to process the answer
num = input('Enter a positive integer: ')
if num.isnumeric() and int(num) > 0:
    answr = is_prime(int(num))
else:
    print('Error! enter a positive integer.')
    quit()

# output
if answr == True:
    print(num, 'is a prime number.')
else:
    print(num, 'is NOT a prime number.')
