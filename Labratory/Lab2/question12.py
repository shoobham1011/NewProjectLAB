'''
given an integer number print its last digit

'''

num = int(input('enter the number : '))

last_digit = num % 10

print(last_digit)

a = str(int(input('enter the number')))
b = len(a)
print(a[b-1])