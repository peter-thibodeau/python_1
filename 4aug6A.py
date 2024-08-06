from math import sqrt
print('CALCULATE THE DISTANCE BETWEEN TWO POINTS')

# get x1
try:
    xone = input('Enter point x1: ')
    x1 = float(xone)
except:
    print('Error! enter numbers only')
    quit()

# get x2
try:
    xtwo = input('Enter point x2: ')
    x2 = float(xtwo)
except:
    print('Error! enter numbers only')
    quit()

# get y1
try:
    yone = input('Enter point y1: ')
    y1 = float(yone)
except:
    print('Error! enter numbers only')
    quit()

# get y2
try:
    ytwo = input('Enter point y2: ')
    y2 = float(ytwo)
except:
    print('Error! enter numbers only')
    quit()

# return answer
length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
answer = '{:,.2f}'.format(length)
print(answer)