age = float(input('How old are you? '))
if age < 18 and age >= 0:
    print('too young, sorry')
elif age >= 18 and age <= 21:
    print('wristband')
elif age > 21 and age <120:
    print('normal entry')
else:
    print('Enter a valid number')