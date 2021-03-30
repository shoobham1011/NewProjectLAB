'''
Given the integer N - the number of minutes that is passed since midnight -
 how many hours and minutes are displayed on the 24h digital clock?
The program should print two numbers: the number of hrs (between 0 and 23) and the number of minutes (between 0 and 59).
'''

N= int(input('enter the minutes passed since midnight:'))

hours =(N//60)
minutes =(N%60)

print(f'The hours is {hours}.')
print(f'The minutes is {minutes}.')
print(f'Its {hours}:{minutes} now.')