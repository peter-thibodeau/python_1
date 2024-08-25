print('CURRENCY CONVERTER')

# get dollars
dollars = input("Enter US dollars and cents (don't use a dollar sign): ")
try:
    dol = float(dollars)
except:
    print('Error! enter numbers only')
    quit()

# convert dollars to desired currency
currency = input('Choose a currency to exchange the dollars: AUS, CAN, EURO, OR GBP ')
if currency == 'AUS':
    curr = dol * 1.52691
    country = 'Australian dollars.'
elif currency == 'CAN':
    curr = dol * 1.37338
    country = 'Canadian dollars.'
elif currency == 'GBP':
    curr = dol * 0.78670
    country = 'British pounds.'
elif currency == 'EURO':
    curr = dol * 0.92
    country = 'Euros.'
else:
    print('Error! you can only select the currencies listed.')
    quit()

# return answer
c = '{:,.2f}'.format(curr)
print(dol, 'US dollar(s) can be exchanged for', c, country)