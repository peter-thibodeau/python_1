print('SIMPLE INTEREST CALCULATOR')

# get primary amount
principle = input('Enter primary amount (whole number with no dollar sign or comma(s)): ')
try:
    p = int(principle)
except:
    print('Error! numbers only')
    quit()

# get interest rate
rate = input('Enter interest rate (number with at least one decimal place): ')
try:
    r = float(rate)
except:
    print('Error! numbers only')
    quit()

# get time period
time = input('Enter time period in years (whole number): ')
try:
    t = int(time)
except:
    print('Error! numbers only')
    quit()

simple_interest = (p * r * t) / 100

# print answer
si = '${:,.2f}'.format(simple_interest)
print('The simple interest is: ', si)