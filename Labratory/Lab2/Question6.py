'''
weight converter:
Input the weight of the person in either in kg or pound(lbs).
If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''

weight_1 = float(input('enter your weight in kg or lbs'))
weight_2 = input('kg or lbs')
pound = 2.2

if weight_2 == 'kg':
    convert = weight_1*pound
    print(f'you are {convert}lbs')
elif weight_2 == 'lbs':
    convert2 = weight_1 / 2.2
    print(f'you are {convert2}kg')
else:
    print("OK")





