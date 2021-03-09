'''
Solve each of the following problem using python scripts.make sure you use an appropriate variable names and comments.
when there is final answer have the python print it to the screen
A person's body mass BMI id defined as:
 BMI: mass in kg /(height in meter)**2
'''

mass_in_kg = float(input('enter the mass'))
height_meter = float(input('enter the height'))

BMI = ( mass_in_kg / (height_meter)**2 )

print(f'The BMI index of a person is {BMI}')
