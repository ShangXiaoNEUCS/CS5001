# Project 7
# Hosoya Triangle
# Shang Xiao
# March 22, 2022

def computeTriangle(levels):
    ''' This function is recursive.  It will compute the levels of Hosoya's triangle.
    It does NOT print Hosoya's triangle.  Remember that each location in the
    triangle is the sum of the two diagonally above it with the top two rows being:
    1
    1 1
    Input: The number of rows to generate
    Output: The triangle as a list of lists.'''
    # if the levels is a negative number of 0, nothing should be in the triangle
    # return an empty list
    if levels <= 0:
        return []
    # the first three level should be hard code
    if levels == 1:
        return [[1]]
    if levels == 2:
        return [[1], [1, 1]]
    if levels == 3:
        return [[1], [1, 1], [2, 1, 2]]
    # first calculate the triangle above this level
    triangle = computeTriangle(levels - 1)
    # add an empty level
    triangle.append([])
    # first two number in this level is two sum of two above it
    triangle[-1].append(triangle[-2][0] + triangle[-3][0])
    triangle[-1].append(triangle[-2][1] + triangle[-3][1])
    for i in range(2, levels):
        # other number is the sum of left one in the previous level and the left 2 one in the previous 2 level
        triangle[-1].append(triangle[-2][i - 1] + triangle[-3][i - 2])
    return triangle
    pass

def printTriangle(triangle, levels):
    ''' This function will print a left justified copy of Hosoya's triangle.
    Input: triangle - the values to be printed, levels - the height of the triangle
    Output: NONE'''
    # if the number of levels is negative or 0, nothing should be printed
    if levels <= 0:
        return
    i = 0
    # level i should have i + 1 numbers
    for level in triangle:
        i += 1
        assert (len(level) == i)
    for levels in triangle:
        for item in levels:
            # each item in the same level is splitting with a space
            print(item, end = " ")
        # each level should end with a newline
        print("")
    pass

def main():
    '''This is the main control function for the program.
    You should ask the user how many levels and then compute the triangle
    recursively. Then you should print the triangle.'''
    # ask for the level
    levels = int(input("Please enter the levels of triangle to be printed: "))
    # print the triangle
    printTriangle(computeTriangle(levels), levels)

if __name__ == '__main__':
    main()