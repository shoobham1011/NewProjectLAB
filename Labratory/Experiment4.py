'''N student take K apples and distribute them among each other evenly.
The remaining (the individual) part remains in the basket. How many apples will each single student get?
How many apples will remain in basket? The program reads the numbers N and K. It should print the two answers for the questions above.'''


N=int(input('enter the number'))
K=int(input('enter the number'))
D=(K/N)
R=(K%N)
print(f'each student got {D}')
print(f'the remaing apples are{R}')



