'''
A school decided to replace the desks in three classrooms.
Each desk sits two students. Given the number of student in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers : the numbers of the students in each of the classes is a,b and c respectively.
In the first test there is three groups. The group has 20students and thus needs 10desks,
the second group has 21 students, so they can get by with no fewer than 11desks.
11desks are also enough for third group of 22students. So, we need 32 desks in total.
'''

students_class1 = int(input('enter the number of students in first class : '))
students_class2 = int(input('enter the number of students in second class : '))
students_class3 = int(input('enter the number of students in third class : '))

desk_class1 = (students_class1 // 2)
print(f'The required number of desks for first class is {desk_class1}.')
desk_class2 = (students_class2 // 2)
print(f'The required number of desks for the second class is {desk_class2}.')
desk_class3 = (students_class3 // 2)
print(f'The required number of the desks for the third class is {desk_class3}.')

remain_class1 = (students_class1 % 2)
print(f'Remaining desk for the first class is {remain_class1}.')
remain_class2 = (students_class2 % 2)
print(f'Remaining desk for the second class is {remain_class2}.')
remain_class3 = (students_class3 % 2)
print(f'Remaining desk for the third class is {remain_class3}.')

Total_desks = (desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3)
print(f'The total number of desks that can be purchased is {Total_desks}.')





