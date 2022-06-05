# CS 5001
# Shang Xiao
# Feb 16, 2022
# testGuessMyNumber.py for project04

from guessMyNumber import *

def print_guesstime_test():
    # we test this function to see if it returns the desired output, I used 4 sets of data to test this function
    testdata = [
        # The first set is [5, 1]
        [5, 1, "You've guessed 5 times, the last time you guessed: 1"]
        # The second set is [6, 10]
        ,[6, 10, "You've guessed 6 times, the last time you guessed: 10"]
        # The third set is [6, 10]
        ,[1000, 100000, "You've guessed 1000 times, the last time you guessed: 100000"]
        # The fourth set is [100, None]
        ,[100, None, "This is your first guess"]
    ]
    i = 0
    # use similar implementation introduced in our Tuesday class
    # using while loop to check each of the four sets above:
    # if the two parameters entered (as data[0] and data[1] respectively)
    # returns the corresponding strings (data[2]) correctly
    while i < len(testdata):
        data = testdata[i]
        if print_guesstime(data[0], data[1]) != data[2]:
            print("print_guesstime is not correct")
            return
        i += 1
    print("print_guesstime is correct")


# same logic and implementations for all three other functions
def print_prompt_test():
    # create 4 sets of numbers, for each set, create three numbers as three parameters in print_prompt_test()
    testdata = [
        [5, 1, 10, "Getting colder"]
        , [6, 10, 11, "Getting hotter"]
        , [1, 3, 2, "Same difference"]
        , [1, 5, 5, "Getting hotter"]
    ]
    i = 0
    # use similar implementation introduced in our Tuesday class
    # using while loop to check each of the four sets above:
    # if the three parameters entered (as data[0], data[1], and data[2] respectively)
    # returns the corresponding strings (data[3]) correctly
    while i < len(testdata):
        data = testdata[i]
        if print_prompt(data[0], data[1], data[2]) != data[3]:
            print("print_prompt is not correct")
            return
        i += 1
    print("print_prompt is correct")

def mininumb_guess_time_test():
    # create 4 sets of numbers, for each set, create three numbers as three parameters in mininumb_guess_time_test()
    testdata = [
        [1, 10, 5, 1]
        , [1, 10, 7, 4]
        , [1, 3, 2, 1]
         , [1, 2, 1, 1]
    ]
    i = 1
    # use similar implementation introduced in our Tuesday class
    # using while loop to check each of the four sets above:
    # if the three parameters entered (as data[0], data[1], and data[2] respectively)
    # returns the corresponding strings (data[3]) correctly
    while i < len(testdata):
        data = testdata[i]
        if mininumb_guess_time(data[0], data[1], data[2]) != data[3]:
            print("mininumb_guess_time is not correct")
            return
        i += 1
    print("mininumb_guess_time is correct")



def get_position_test():
    # create 4 sets of numbers, for each set, create two numbers as two parameters in get_position_test()
    testdata = [
        [1, 10, "Too low"]
        , [11, 10, "Too high"]
        , [1, 1, "You've got it!"]
        , [-1, 2, "Too low"]
    ]
    i = 0
    # use similar implementation introduced in our Tuesday class
    # using while loop to check each of the four sets above:
    # if the three parameters entered (as data[0] and data[1] respectively)
    # returns the corresponding strings (data[2]) correctly
    while i < len(testdata):
        data = testdata[i]
        if get_position(data[0], data[1]) != data[2]:
            print("get_position is not correct")
            return
        i += 1
    print("get_position is correct")

if __name__ == '__main__':
    print_guesstime_test()
    print_prompt_test()
    get_position_test()
    mininumb_guess_time_test()
