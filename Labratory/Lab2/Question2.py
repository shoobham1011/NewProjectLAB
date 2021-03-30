'''
WAP which accepts marks for four students and display total marks , percentage and grade
HINTS: More than 70%->distinction, more than 60% ->first, more than 40%->pass, less than 40%-> fail.
'''

marks1 = int(input('Enter the marks: '))
marks2 = int(input('Enter the marks: '))
marks3 = int(input('Enter the marks: '))
marks4 = int(input('Enter the marks: '))

Total_marks = marks1 + marks2 + marks3 + marks4
grade = (Total_marks * 100)/400

if 70 <= grade:
    print('distinction')
elif 60 <= grade <= 70:
    print('first division')
elif 40 <= grade <= 60:
    print('Passed')
elif grade <= 40:
    print('Failed')

