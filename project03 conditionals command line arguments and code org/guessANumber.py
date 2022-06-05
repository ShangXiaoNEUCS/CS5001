# Shang Xiao
# Feb 4, 2022
# CS5001
# guessANumber for project03

import random
import string

def getSuit():
    '''As per request, we first write a function that uses random.choice to randomly
    pick one of the four suits for us.
    Function name: getSuit
    Parameter: four strings
    Returns: a string - using random.choice to pick a suit'''
    x = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
    return (random.choice(x))

def getValue():
    '''As per request, we then write a function that uses random.choice to randomly
    pick one of the 13 values for us.
    Function name: getValue
    Parameter: 13 strings
    Returns: a string - using random.choice to pick a value in one of the suits'''
    y = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    return (random.choice(y))

def printCard(value, suit):
    '''Lastly we make a function that combines the random results from getSuit and getValue.
    Function name: printCard
    Parameter: two strings returned by getSuit() and getValue()
    Returns: nothing'''
    print(value + " of " + suit)

if __name__ == '__main__':
    '''Store all of the three function values by assigning them with seperate varaibles.'''
    value = getValue()
    suit = getSuit()
    printCard(value, suit)

    '''Ask the user to input a colour by using the input function'''
    userGuess = input("Make a choice and type 'red' or 'black'. No capitalized letter pls:")

    # Start by two suits in red colour, if user also picked red and the printCard random
    # result is also red, inform the user that they picked red and the random chosen card
    # happens to be red as well. Otherwise, if user picked black, inform the use that they
    # picked black and the random chosen card happens to be red, which is different from
    # their pick
    if suit == "Diamonds" or suit == "Hearts":
        if userGuess == "red":
            print("The random card is")
            printCard(value, suit)
            print("You picked red, and the random card is in red")
        else:
            print("The random card is")
            printCard(value, suit)
            print("You picked black, but the random card is in red")

    # Since we have already covered all the possibilities when user pick red, now it is
    # time for us to complete the program by finalizing the senarios when user pick black.
    # Start by two suits in black colour, if user also picked black and the printCard rondom
    # result is also blck, inform the user that they picked black and the random chosen card
    # happens to be black as well. Otherwise, if user picked red, inform the user that they
    # picked red and the random chosen card happens to be black, which is different from
    # their pick.
    else:
        if userGuess == "black":
            print("The random card is")
            printCard(value, suit)
            print("You picked black, and the random card is in black")
        else:
            print("The random card is")
            printCard(value, suit)
            print("You picked red, but the random card is in black")


