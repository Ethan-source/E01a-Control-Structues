#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
color = ''
count = 0
while (color != 'red'):
    color = input("what is your favorite color?")
    color = color.lower().strip()
    count = count + 1               # You can also write this as count += 1
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')
print('You guessed it in {0} tries!'.format(count))