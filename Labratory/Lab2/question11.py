'''
for given integer x , print true if it is positive
print false if negative and print zero if it is 0

'''

x = int(input('enter the number : '))


if x == 0:
    print('ZERO')

elif x > 0:
    print('Positive')
elif x < 0:
    print('Negative')