command = ""
started = False
applied = True
removed = False
while True:
    command = input('>: ').upper()
    if command == 'start':
        if started:
             print('car is already started!.....')
        else:
            started = True
            print('car started!......')
    elif command == 'stop':
        if not started:
             print('car is already stopped!....')
        else:
             started = False
             print('car stopped!.....')
    elif command == 'help':
            print("""
            start = to start the car
            stop = to stop 
            quit = to quit
            """)
    elif command == 'apply':
            if applied:
                print('gear one already applied!.....')
            else:
                applied = True
                print('gear one applied')
    elif command == 'remove':
            if not remove:
                print('print gear two already removed!.....')
            else:
                remove = True
                print('gear removed!......')
    elif command == 'quit':
        break
        print('sorry i dont understand that!.....')
                    