import random
print('''==========================================================
                < Guessing Game >
==========================================================
''')

num = random.randint(1, 100)
pick = None

while True:
    pick = input('➡  Choose a number between 1 and 100\n  ')
    pick = int(pick)
    if pick > num:
        print('⬆ Too high, Choose another\n  ')
    elif pick < num:
        print('⬇ Too low, Choose another\n  ')
    else:
        print('✔ Thats the answer!!!')
        play_again = input('Wanna play again? (y/n)  ')
        if play_again == 'y':
            num = random.randint(1, 100)
            pick = None
        else:
            print(' Ok, bye')
            break
