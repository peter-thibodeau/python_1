print('CALCULATE BMI')

# get weight
weight = input('Enter your weight in kilograms: ')
try:
    w = float(weight)
except:
    print('Error! enter numbers only')
    quit()

# get height
height = input('Enter your height in meters: ')
try:
    h = float(height)
except:
    print('Error! enter numbers only')
    quit()

# return answer
bmi = w/h**2
answer = '{:,.2f}'.format(bmi)
print('Your BMI is: ', answer)