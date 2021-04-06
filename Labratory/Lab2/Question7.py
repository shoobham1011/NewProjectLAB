'''
game finding a secret number within 3 attempts using while loop
'''

sec_number = 3

i = 1

while i <= 3:
    give = int(input('enter the number '))
    i +=  1

    if give == sec_number:
        print('you got the right number')
        break
else:
        print('you are wrong')