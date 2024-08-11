print('AVERAGE OF THREE GRADES')

# input
inp1 = input('Enter the first numerical grade: ')
inp2 = input('Enter the second numerical grade: ')
inp3 = input('Enter the third numerical grade: ')

# verify input
if inp1.isnumeric() and len(inp1)<3 and inp1 != '00' and int(inp1) >0:
    grade1 = int(inp1)
    if inp2.isnumeric() and len(inp2) <3 and inp2 != '00' and int(inp2) >0:
        grade2 = int(inp2)
        if inp3.isnumeric() and len(inp3) <3 and inp3 != '00' and int(inp3) >0:
            grade3 = int(inp3)
else:
    print('Error! grades must be one, or two digit numbers.')
    quit()

# processing and output
avg_grade = (grade1 + grade2 + grade3)/3
if avg_grade >= 90:
    print('Your grade is an A')
elif 80 <= avg_grade <= 89:
    print('Your grade is a B')
elif 70 <= avg_grade <= 79:
    print('Your grade is a C')
elif 60 <= avg_grade <= 69:
    print('Your grade is a D')
elif avg_grade < 60:
    print('Your grade is an F')


