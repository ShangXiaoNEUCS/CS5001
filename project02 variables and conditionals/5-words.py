# Shang Xiao
# Jan 26, 2022
# CS5001
# Algorithm 2 for Lab 2

# We begin by asking the user to input five words, we assign each word as variable a,b,c,d,e
def five():
    a = str(input("Enter first word: "))
    b = str(input("Enter second word: "))
    c = str(input("Enter third word: "))
    d = str(input("Enter fourth word: "))
    e = str(input("Enter fifth word: "))

# We have now collected the data set from the user and we write below code to call this array "data"
    data = [a, b, c, d, e]

# In my algorithm here it is a combination of a "bubble sort" with "guess and try"
# Apply guess and try first. We first assume that the maximum value here is the first value in array
# data and if the max value is not the first
# value, we then assume/guess the max value is the second value and so on until we reach the fifth value in the array.
# During this process, each of the value from a to e has already been guessed once to be the max value and will be
# proceeded along the order of the following if statements. At this point we have found the max value in this array,
# thus we eliminated the first value to guess, four to go
    max = 0
    if data[1] > data[max]:
        max = 1
    if data[2] > data[max]:
        max = 2
    if data[3] > data[max]:
        max = 3
    if data[4] > data[max]:
        max = 4
# This is where we implement the bubble sort thinking. At this stage all five value have been compared and at this point
# the system is guessing the the e is the max, and we write the following if statement to tell the system that if e is not
# the max here, then we switch both e and the max value's position once, so that the max value will be set to be the last
# position in array data. Since using this algorithm will always allocate the maximum value in an array to the last position
# it was as if something sinking under the sea slowing floating towards the sea surface, just like a bubble, hence the
# name bubble sort
    if max != 4:
        data[4], data[max] = data[max], data[4]

# We repeat the above algorithm, but this time since we have already decided the max value set to the last position of
# the array, it is time to find the second largest value in the array, we use the same logic to compare if the max value
# is a or b or c or d, and if d is not the max, switch the max position to the last position
    max = 0
    if data[1] > data[max]:
        max = 1
    if data[2] > data[max]:
        max = 2
    if data[3] > data[max]:
        max = 3
    if max != 3:
        data[3], data[max] = data[max], data[3]

# Same idea again, we decide the third largest value in the array
    max = 0
    if data[1] > data[max]:
        max = 1
    if data[2] > data[max]:
        max = 2
    if max != 2:
        data[2], data[max] = data[max], data[2]

# We find the fourth largest in the array. At this point, we have found the largest value, the second largest value, the
# third largest value, the fourth largest value. It is time to return our algorithm result to the user
    max = 0
    if data[1] > data[max]:
        max = 1
    if max != 1:
        data[1], data[max] = data[max], data[1]

# Return our final result to user
    print(data)


five()

