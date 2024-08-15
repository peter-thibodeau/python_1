print('IS IT A PALINDROME?')

# input
inp = input('Enter a word, phrase, letters, or numbers: ')

# processing and printing result
lwr = inp.lower()
no_spaces = lwr.replace(" ", "")
l1 = len(no_spaces)
l2 = len(no_spaces) // 2 # handle input whose length is odd
x = 0

for i in range (0, l2):
    if no_spaces[i] == no_spaces[l1-i-1]:
        x += 1
    else:
        print(inp, 'is not a palindrome.')
        quit()
if x == l2: # passed
    print(inp, 'is a palindrome')
