import random

print('-----------------------------------')
print('        GUESS THAT NUMBER GAME')
print('-----------------------------------')
print()

while True:
    the_number = random.randint(0, 100)
    print(the_number)
    guess_text = input('Guess a number between 0 and 100: ')

    '''
    if guess_text == [A - Za - z]:
        print('Number must be between 0 and 100! Try again.')
        continue
    elif guess_text == "":
        print('Number must be between 0 and 100! Try again.')
        continue
    '''
    guess = int(guess_text)

    if guess > 100:
        print('Number must be between 0 and 100! Try again.')
    elif guess < 0:
        print('Number must be between 0 and 100! Try again.')
        continue
    elif guess == the_number:
        print('The number is {}'.format(the_number))
        break
    else:
        print('Number must be between 0 and 100! Try again.')
        continue
