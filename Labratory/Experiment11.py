"""
write a python program to convert seconds to day , hour , minutes and seconds.
"""

seconds = int(input('enter the second'))

minutes = seconds // 60
hour = minutes // 60
day = hour // 24

print(f'day is {day} : hour is {hour} : minutes is {minutes} : seconds is {seconds}')


