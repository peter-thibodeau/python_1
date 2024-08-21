print('IS IT A PALINDROME?')

# input
inp = input('Enter a word, phrase, letters, or numbers: ')

# create variables
l1 = len(no_spaces)
l2 = len(no_spaces) // 2 # handle input whose length is odd
x = 0

def proc_inp(inp):
    """ normalize input """
    lwr = inp.lower()
    return lwr.replace(" ", "")

def is_palindrome(no_spaces):
    """ determine if input is a palindrome"""
    for i in range (0, l2):
        if no_spaces[i] == no_spaces[l1-i-1]:
            x += 1
        else:
            print(inp, 'is not a palindrome.')
            quit()

no_spaces = proc_inp(inp)

if x == l2: # passed
    print(inp, 'is a palindrome')
