# Project 5
# Spaceman Implementation
# Shang Xiao
# February 22, 2022


# implementation of the spaceman game,
# begin by importing the random module because we need to use random.choice() later
import random

def pick_random_word():
    '''Pick_random_word will create a word list, chooose a random word and return it
    Input: None
    Output: A random word from the list
    '''
    # create a list of 20 words between 5 and 15 characters long
    list = ['tomato', 'google', 'twitch', 'canada', 'apple'
            , 'soccer', 'toyota', 'adidas', 'forever', 'banana'
            , 'potato', 'goodbye', 'pepsi', 'twitter', 'costco'
            , 'noodle', 'amazon', 'samsung', 'toronto', 'youtube']
    # use random.choice() to pick a random word from the list
    return random.choice(list)

def create_hidden_word(rand_word):
    '''create_hidden_word will create an obfuscated version of the random word
    Input: The random word
    Output: An obfuscated version of the word (ie banana would return ******
    '''
    # pick * to save as a hidden word that will indicate the length of the random word
    return '*' * len(rand_word)

def word_found(rand_word, hidden_word):
    '''word_found will detect whether the random word has been uncovered
    Input: the random word and the hidden version of the word
    Output: True if the hidden word has all been revealed, False otherwise
    '''
    # hopefully, the user will eventually find all the characters in the word. This function will end the game and
    # prompt the user that they had won if they have uncovered the random word
    if rand_word == hidden_word:
        return True
    else:
        return False

def replace_character(rand_word, hidden_word, user_guess):
    '''Replaces all the occurences of user_guess in hidden_word with user_guess
    Input: the random word, the hidden word so far, and the user guess
    Output: the new hidden word
    '''
    i = 0
    # use a new_word to save the most recent guessing character
    new_word = ''
    # check every character whether it is already been uncovered, not uncovered or is going to be uncovered
    while i < len(rand_word):
        # if this character is guessed correctly, it will be uncovered
        if rand_word[i] == user_guess:
            new_word += rand_word[i]
        # if this character has already been uncovered, replace * with the uncovered letter
        elif hidden_word[i] != '*':
            new_word += hidden_word[i]
        # otherwise, keep the character as '*'
        else:
            new_word += '*'
        i += 1
    return new_word

def main():
    '''Main game playing location'''
    # Here I tried my best to make the game as user-friendly as possible. And since 6 wrong attempts limitation seems
    # a bit hard, I wanted to throw some hints to the user to make the game more playable
    print("Welcome to spaceman!\n"
          "Hint: word topics come from brands, foods, companies, sports, and expressions etc. ")
    print("Note: all characters, including the first character, are in lowercases only")
    print("You are allowed 6 wrong guesses")
    # pick a random word from 'list' and save it in random_word
    random_word = pick_random_word()
    # using create_hidden_word(random_word) change the random word into hidden word
    hidden_word = create_hidden_word(random_word)
    # set up maximum guess time, which is 6
    remain_time = 6
    # create a variable called win to determine whether the user had won
    win = 0
    print('The word is {0}'.format(hidden_word))

    # Setting up loop stuff
    while remain_time > 0:
        # ask user to input
        user_guess = input('A lowercase character you want to guess for this time: ')
        # replace the uncovered characters from the hidden word
        new_word = replace_character(random_word, hidden_word, user_guess)

        # when user uncovered a new character, new_word will not be the same as the previous hidden_word, for example,
        # for word apple, if the current user progress is a***e, and user uncovered a character this time, say p, then
        # the new_word now becomes app*e, which is not the same as a***e, this means that user had successfully uncovered
        # something, thus we write the following condition:
        if new_word != hidden_word:
            print("Nice, '{0}' is in the random word!\n"
                  "The word is now {1}".format(user_guess, new_word))


        # when user failed to uncover a new character, new_word will still be the same as the previous hidden_word,
        # for example,
        # for word apple, if the current user progress is a***e, and user failed to uncover a character this time
        # then the new_word will still be a***e, which is the same as a***e, thus we write the following condition:
        else:
            print(
                "Sorry, '{0}' is not in the random word.\n"
                "The word is still {1}".format(
                    user_guess, hidden_word))
            print('This is your {0}/6 wrong guess(es)'.format(6 - remain_time + 1))
            remain_time -= 1
        hidden_word = new_word

        # when user have uncovered all characters, they had won
        if word_found(random_word, hidden_word):
            win = 1
            break

    # prompt user the end game result
    if win == 1:
        print('Congratulations! You win! The word is {0}.'.format(random_word))
        print("You've guessed {0}/6 wrong time(s) in total.".format(6 - remain_time))
    else:
        print('Sorry, you lost. The word is {0}.'.format(random_word))


if __name__ == "__main__":
    main()