def start():
    '''starts the game and defines name and class'''
    valid_classes = ['warrior', 'mage', 'rogue']
    greeting = 'Hello adventurer, welcome to the mysterious mansion.'

    print(greeting)
    name = str(input('Enter your name: '))
    clas = ''
    while clas not in valid_classes:
        clas = str(input('Choose your class (warrior, mage, rogue): ')).casefold()
        if clas not in valid_classes:
            print('Enter a valid class!')
    return name, clas