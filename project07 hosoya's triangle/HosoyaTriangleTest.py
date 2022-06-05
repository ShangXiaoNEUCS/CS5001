# Project 7
# Hosoya Triangle Test
# Shang Xiao
# March 22, 2022

from HosoyaTriangle import *
def computeTriangleTester():
    testcase = [[-10, []]
        , [-1, []]
        , [0, []]
        , [1, [[1]]]
        , [2, [[1], [1, 1]]]
        , [5, [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3], [5, 3, 4, 3, 5]]]]
    for data in testcase:
        triangle = computeTriangle(data[0])
        assert(triangle == data[1])

def printTriangleTester():
    testcase = [[[], -10]
        , [[], -1]
        , [[], 0]
        , [[[1]], 1]
        , [[[1], [1, 1], [2, 1, 2], [3, 2, 2, 3], [5, 3, 4, 3, 5]], 5]]
    for data in testcase:
        triangle = printTriangle(data[0], data[1])

def main():
    computeTriangleTester()
    printTriangleTester()
    print("All tests passed")

if __name__ == '__main__':
    main()
