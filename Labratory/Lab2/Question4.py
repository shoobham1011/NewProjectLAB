'''
If the temperature is greater than 30
its a hot day otherwise if its less than 10:
its a cold day: otherwise;
its neither hot nor cold
'''

temperature =int(input('enter the temp :'))

if 30 <= temperature:
    print('its a hot day')
elif temperature <= 10:
    print('Its a cold day')
else:
    print('its a moderate day')