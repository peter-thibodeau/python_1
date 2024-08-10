print('IS IT A LEAPYEAR?')

# input
year = ''
inp = input('Enter a four-digit year: ')
if inp.isnumeric() and len(inp)==4:
    year = int(inp)
else:
    print('Error! must be a four digit number.')
    quit()

# process and output
if year % 4 == 0:
    print('Yes, that is a leap year.')
elif year % 100 == 0 and year % 400 == 0:
    print('Yes, that is a leap year.')
else:
    print('No, that is not a leap year.')
