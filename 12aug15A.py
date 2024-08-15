print('PRINT A RIGHT TRIANGLE')

# input verification
inp = input('Enter the number of rows: ')
if inp.isdigit():
    num = int(inp)
else: # a non-numeric character including a dash before a number is an error
    print('Error! enter a positive whole number.')
    quit()

# get the character to print
char = input('Enter a character to print: ')

# processing and printing a right triangle
for i in range(0, num):
    for j in range(0, i+1):
        print(char, end="")
    print() # overrides end="" to start a new row
