print('IS IT A PALINDROME?')

# input
inp = input('Enter word, phrase, letters, or numbers: ')

# processing and printing result
lwr = inp.lower()
no_spaces = lwr.replace(" ", "")
l1 = len(no_spaces)
l2 = len(no_spaces) // 2
x = 0
flag = ''

def is_palindrome(no_spaces, x):
    """ determine if input is a palindrome """
    if x == l2:
        print(inp, 'is a palindrome')
    elif no_spaces[x] == no_spaces[l1-x-1]:
        is_palindrome(no_spaces, x+1)
    else:
        print(inp, 'is not a palindrome')

# call function to start processing
is_palindrome(no_spaces, x)