# Shang Xiao
# Jan 26, 2022
# CS5001
# Algorithm 1 for Lab 2

def z():

    # we begin by asking the user to input 3 numbers
    a = int(input("Please enter your first number here:"))
    b = int(input("Please enter your second number here:"))
    c = int(input("Please enter your third number here:"))

    # we apply a "guess and check" algorithm here, "g&c" is a very powerful algorithm that
    # I have learned through Module 2
    # we first assume that the first number is the biggest, if a is the biggest, return a is the biggest
    max = a
    # there were two possiblities, a was the biggest and a was not the biggest, if a was not the biggest,
    # then we test if b is the biggest, and if it is, return b is the biggest
    if b > a:
        mx = b
    # again, there were two possiblities, b was the biggest and b was not the biggest, if b was not the biggest,
    # then we test if c is the biggest, and if it is, return c is the biggest
    if c > max:
        max = c
    # we output our final result to the user
    print("The biggest number is", max)


    # same logic for finiding the smallest number, we substitute max to min
    # we first assume that the first number is the smallest, if a is the smallest, return a is the smallest
    min = a
    # there were two possiblities, a was the smallest and a was not the smallest, if a was not the smallest,
    # then we test if b is the smallest, and if it is, return b is the smallest
    if b < a:
        min = b
    # again, there were two possiblities, b was the smallest and b was not the smallest, if b was not the smallest,
    # then we test if c is the smallest, and if it is, return c is the smallest
    if c < min:
        min = c
    # we output our final result to the user
    print("The smallest number is", min)


    # compute the average is simple, just add up all three numbers and then divide them by 3
    average=(a+b+c)/3
    # we output our final result to the user
    print("The average is", int(average))


z()
