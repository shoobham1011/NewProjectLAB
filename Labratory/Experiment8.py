'''
you live 4miles from university. The bus driver drives at 25mph but spends 2minute at each stop of ten stops on the way.
how long will the bus journey takes? alternatively you could run to university. you jog the first mile at 7mph then run the
next 2 at 15mph before jogging the last at 7mph again. will this be quicker or slower than bus ?
'''

uni_distance = 4                                  #miles
driver_speed = ( 4 / 25) * 60
stop_time = (2 * 10)                             #minutes

bus_time = (driver_speed + stop_time)

print(f'the driver takes {bus_time} minute to reach university')


first_run = (1/7) * 60
second_run = (2/15) * 60
third_run = (1/7) * 60

Walk_time = ( first_run + second_run + third_run)

print(f'time taken by running is {Walk_time}')

if bus_time  > Walk_time :
    print('taking the bus slower than running')
else:
  print('taking the bus is faster than running')