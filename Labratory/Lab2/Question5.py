'''
If names is less than 3 characters long- name must be atleast 3 characters
otherwise if its more than 50characters-name must be maximum of 50 characters
otherwise - name looks good
'''

name = input('enter your name :')
count = len(name)

if count < 3:
    print('it should be more than 3 characters.')
elif 50 < count:
    print('name must be maximum of 50 characters')
else:
    print('name looks good')