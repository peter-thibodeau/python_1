print('CONVERT HOURS TO MINUTES AND SECONDS')

# get hours
hours = int(input('enter number of hours: '))
if hours > 0:
    pass
else:
    print('Positive numbers only')
    quit()

# calc minutes
mins = hours * 60
m = '{:,.0f}'.format(mins)

# calc seconds
secs = hours * 60**2
s = '{:,.0f}'.format(secs)

print(hours, 'hours equals', m, 'minutes or', s, 'seconds')