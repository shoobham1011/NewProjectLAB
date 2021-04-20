'''
9. CHeck whether the given year is leap year or not. if year is leap print 'LEAP YEAR' else print
'COMMON YEAR'

'''

year = 1996

if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
    print('LEAP YEAR')

else:
    print('COMMON YEAR')