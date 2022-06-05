# Shang Xiao
# Feb 4, 2022
# CS5001
# oddOrEven for project03

import sys

# calculate whether a number is odd or even
def oddOrEven( number ):
    '''Function name: oddOrEven
    Parameter: one number - string
    returns: nothing'''
    print('determining if ' + str(number) + ' is odd or even:')

    # if statement
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")

def main():
    # assign values to variables. The purpose of this line is what descripted in step 5: catching
    # user errors. We pick a default value and store it in a variable which we created. In this case, we call
    # it "my_number", so that no matter what user type in as inputs, the program will always run with input set to 10.
    my_number = 10

    # check for user input
    if len( sys.argv ) > 1:
    # re-assign the value if the user provided one. If user provided a correct value, then the user input can override
    # the default value which was set to 10.
        my_number = int( sys.argv[1] )

    # call the function
    oddOrEven(my_number)


if __name__ == "__main__":
    main()