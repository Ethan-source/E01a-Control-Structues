#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #Prints "greetings" in the terminal as the introduction.
colors = ['red','orange','yellow','green','blue','violet','purple'] #specifies all of the potential answers
play_again = '' #specifies which character allow you to play again or not play again.
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #While loop that gvies you the option to continue to play even after you win.
    match_color = random.choice(colors) #Randomizes the "Match color" of what color allows you to win the game.
    count = 0   #Counts each attempt 
    color = ''  #specifies what can be the potential colors.
    while (color != match_color):  #while loop that askes you what your favorite color is again if you don't get the right answer.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()   #allows for characters to be upper and lowercase, and gets rid of the whitespaces in your answer.
        count += 1  #Adds 1 for every time you get a wrong answer 
        if (color == match_color): #if your answer is the match color then you proceed with the code below
            print('Correct!')   #prints correct if your color was the match color
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #Prints "sorry try again" and uses the count to see how many times you attempted the wrong answers.
    print('\nYou guessed it in {0} tries!'.format(count))#If you got the right answer it will tell you how many times it took you to get to the right answer
    if (count < best_count): #If statement saying if it took you less attempts to solve the puzzle than the best count it will print the statement below
        print('This was your best guess so far!') #prints "This was your best guess so far" in the terminal
        best_count = count  #If the number of attempts it took you to complete the game is the same as the best count, then it will just ask you to play again.
    play_again = input("\nWould you like to play again? ").lower().strip() #allows you to respond to the question "would you want to play again" and allows you to input upper and lowercase letters in addition to taking out the whitespaces.
print('Thanks for playing!') #Prints "thank you for playing" in the terminal once you have completed the puzzle and said you don't want to play again.