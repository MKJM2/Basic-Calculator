import sys
import os

clear = lambda: os.system('cls')


def addition():

    a = int(input('\nPlease give me the first number\n>>> '))
    b = int(input('\nPlease give me the second number\n>>> '))
    print('\n{} + {} equals {}'.format(a, b, a+b))

def substraction():

    a = int(input('\nPlease give me the first number\n>>> '))
    b = int(input('\nPlease give me the second number\n>>> '))
    print('\n{} - {} equals {}'.format(a, b, a-b))

def multiplication():

    a = int(input('\nPlease give me the first number\n>>> '))
    b = int(input('\nPlease give me the second number\n>>> '))
    print('\n{} x {} equals {}'.format(a, b, a*b))

def division():

    a = int(input('\nPlease give me the first number\n>>> '))
    b = int(input('\nPlease give me the second number\n>>> '))
    print('\n{} / {} equals {}'.format(a, b, a/b))

print('______________________________\n')
print('Welcome to a basic calculator!')
print('______________________________')

while True:


    print('\nSupported actions:            ')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multiplication')
    print('4. Division')
    print('0. Exit')
    print('______________________________\n')
    mode = int(input('Choose your desired action:  '))

    if mode == 1:
        addition()
        input('\n\nPress Enter to continue')
        clear()
    elif mode == 2:
        substraction()
        input('\n\nPress Enter to continue')
        clear()

    elif mode == 3:
        multiplication()
        input('\n\nPress Enter to continue')
        clear()

    elif mode == 4:
        division()
        input('\n\nPress Enter to continue')
        clear()

    elif mode == 0:

        break
    else:
        continue
