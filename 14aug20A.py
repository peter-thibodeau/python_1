print('CALCULATE EXPONENTS')

# get input
base = int(input('enter a positive whole number for the number: '))
expon = int(input('enter a positive whole number for the exponent: '))

# process answer
def power(base, expon):
    ans =  base ** expon
    return ans

# verify input
if expon > 0:
    pass
else:
    print('Error! enter a positive number for the exponent.')
    quit()

# output
answer = power(base, expon) # call power function to get answer
print(answer)
