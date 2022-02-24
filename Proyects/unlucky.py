print('''==========================================================
               THE LUCKY GAME
==========================================================
''')
# num = int(input(' - Choose a number between 1 and 20\n    '))

for num in range(1,21):
    if (num == 4 or num == 13):
        x ='unlucky'
    elif num % 2 != 0:
        x = 'odd'
    else:
        x = 'even'

    print(f'{num} is {x}')
