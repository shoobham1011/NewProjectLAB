'''

>help
start - to start the car
stop - to stop the car
quit - to exit
>asd
I don't understand this
>start
car started... ready to go!
>stop
car stopped
>quit
'''

command = ''
started = False

while command != 'quit':
    command = input('>')
    if command == 'quit':
        print('the game has ended')
        break
    elif command  == 'start':
        if started:
            print('the car has already started...')

        else:
            started = True
            print('the car has started....ready to go')
    elif command == 'stop':
        print('car stopped')
    elif command == 'help':
        print('''start - to start the car
        stop - to stop the car
        quit - to exit
        ''')
    else:
        print('i dont understand this shit')
