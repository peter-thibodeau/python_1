print('CALCULATE THE AREA OF A RECTANGLE')

# get length
length = float(input('enter a positive whole number for length: '))
if length > 0:
    l = length
else:
    print('Positive numbers only')

# get width
width = float(input('enter a positive whole number for width: '))
if width > 0:
    w = width
else:
    print('Positive numbers only')

# return answer
print('The area of the rectangle is', l*w)