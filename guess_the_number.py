# Program is 'Guess the number' game.
# Player gets hints if number is geater or lower.

import random as r

number_of_guesses = 0
number =r.randrange(1,20)

while number_of_guesses < 5:
    guess = input('Guess number between 1 and 20. You have five tries. \n')
    # Error handling with non-integer input
    try:
        guess=int(guess)  
        # Error handling with incorrect guess range
        if 0 < guess < 21:
            number_of_guesses += 1
            if guess < number:
                print('This number is greater.')
            elif guess > number:
                print('This number is lower.')
            else:
                break
        else:
            print('The number should be between 1 and 20.')
    except:
        print('Incorrect number. Please type a number.')

if guess == number:
    print('Congratulations! This is the correct number. You have needed only', number_of_guesses, 'tries.')
else:
    print('Unfortunatelly, you have not guessed the correct number. Correct number was', number)
