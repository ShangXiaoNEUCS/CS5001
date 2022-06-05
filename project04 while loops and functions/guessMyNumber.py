# CS 5001
# Shang Xiao
# Feb 16, 2022
# guessMyNumber.py for project04

from random import randint

# Compare user input whity the randomly chosen number, too high if user guess > random;
# too low if user guess < random; else, user win
def get_position(guess, number):
    '''Name: get_position
    Parameter: two numbers (int)
    Return: comparison result (a string)'''
    if guess > number:
        return "Too high"
    elif guess < number:
        return "Too low"
    else:
        return "You've got it!"

# Prompt user how many times of guesses they have already attempted and which guess time is the current one
number = 0
def print_guesstime(guesstime, lastguess):
    '''Name: print_guesstime
    Parameter: two numbers (str)
    Return: guess time (a string)
    '''
    # return the prompt text about the total guessing time and the value last time guessed
    if lastguess != None:
        return "You've guessed " + str(guesstime) + " times, the last time you guessed: " + str(lastguess)
    else:
        return "This is your first guess"


# Prompt the user if they are getting closer to the random value, getting colder if the absolute difference
# of this guess larger than the last guess, same difference if the absolute difference of this guess equal to the
# last guess, else, getting hotter
def print_prompt(lastguess, thisguess, number):
    '''Name: print_prompt
    Parameters: three numbers (int)
    Return: comparison result (a string)'''
    if lastguess != None:
        # if the difference between this guess and the random number is more than the difference betweem last guess
        # and the random number, print getting colder, meaning this guess is further from the random number
        if abs(lastguess - number) < abs(thisguess - number):
            return "Getting colder"
        # same difference, meaning this guess and last guess have the same difference to the actual random number, user is
        # very close to finding the actual random number
        elif abs(lastguess - number) == abs(thisguess - number):
            return "Same difference"
        # if the difference between this guess and the random number is less than the difference betweem last guess
        # and the random number, print getting hotter, meaning this guess is closer to the random number
        else:
            return "Getting hotter"
    else:
        # for the first guess, still need to return a string
        return "The random number is not {0}, Try again!".format(thisguess)


# For a given range, l to r, the midpoint is (l+r)//2. We call get_position(), and use mid as the first parameter,
# and compare it with the second parameter, which is the random number
# if returns too high, then the random number is within range [l, mid - 1];
# if returns too low, then the random number is within range [mid + 1, r];
# else, the random number == mid
# we can use the function to calculate how many times it takes to guess needed for any given range
def mininumb_guess_time(l, r, number):
    '''Name: mininumb_guess_time
    Paramaters: three numbers (int)
    Return: calculation result (a string)'''
    # the number is between l, r
    if l > r:
        # l > r means lower bound is bigger than the upper bound, empty range
        return None
    mid = (l + r) // 2
    if get_position(mid, number) == "Too high":
        # if the random number is lower than mid, then it is in [l, mid - 1], plus one guess time in mininumb_guess_time
        return mininumb_guess_time(l, mid - 1, number) + 1
    elif get_position(mid, number) == "Too low":
        # if the random number is higher than mid, then it is in [mid + 1, r], plus one guess time in mininumb_guess_time
        return mininumb_guess_time(mid + 1, r, number) + 1
    else:
        # returns 1 if the random number is the midpoint number
        return 1


if __name__ == '__main__':
    # prompt the user to enter a range, split by space, " "
    range = input("Please enter a range, split by space, smaller number goes first: ").split()

    # use randint to randomly pick a number within the enterted range
    number = randint(int(range[0]), int(range[1]))

    # set guesstime to 0 since the user has not made any guesses yet
    guesstime = 0

    # set lastguess to None, because the user starts at first guess
    lastguess = None

    # set up the while loop, the loop means if last guess is not the random number,
    # then we repeat forever until user find the random number
    while lastguess == None or lastguess != number:

        # prompt the user how many times they have guessed and which number did they enter for last guess
        print(print_guesstime(guesstime, lastguess))

        # prompt the user to enter a number for this guess
        thisguess = int(input("Your guess for this time: "))
        # for every new guess, guess time +1
        guesstime += 1

        # if user guessed the random number, break the loop and prompt the user that they've got it
        if thisguess == number:
            break

        # if this guess is not the random number, continue to prompt the user using printprompt()
        print(print_prompt(lastguess, thisguess, number))

        # for each new guess, compare this guess with last guess
        print(get_position(thisguess, number))

        # for each new guess, this guess becomes last guess, for example, if this guess is 5, then for next guess,
        # 5 becomes last guess
        lastguess = thisguess

    # prompt the user their final statistics if they've got the random number correctly
    print("You've got it!\n"
          "Your total attempts were: {0}\n"
          "Your guessing pattern was {1}".format(guesstime, "efficient" if(guesstime <= mininumb_guess_time(int(range[0]), int(range[1]), number)) else "not efficient"))
