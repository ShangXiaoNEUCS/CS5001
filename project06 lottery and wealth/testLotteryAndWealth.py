# Project 6
# Lottery and Wealth Simulation Test
# Shang Xiao
# March 8, 2022

from LotteryAndWealth import *
# tester for generateLotteryNumbers()
# since it is a random function, we can just check the length of list and the range of each number
def generateLotteryNumbersTester():
    list = [generateLotteryNumbers() for i in range(10)]
    # assert is used for check whether the argument is True
    # if the argument is False, is statement will stop the program immediately
    for testdata in list:
        assert(len(testdata) == 5)
        for i in testdata:
            assert(1 <= i <= 42)
            assert(testdata.count(i) == 1)

# tester for countMatches()
# the function need arguments we put some hand-made input the test it
def countMatchesTester():
    # generate some testcase to test the program
    testdatas = [[[1, 2, 3, 4, 5], [1, 2, 3, 6, 7], 3]
                , [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 0]
                , [[1, 2, 3, 4, 5], [3, 2, 1, 4, 5], 5]
                , [[1, 2, 3, 4, 5], [1, 2, 3, 6, 7], 3]
                , [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 5]
                , [[1, 2, 3, 4, 5], [6, 3, 2, 1, 7], 3]]
    for testdata in testdatas:
        assert(countMatches(testdata[0], testdata[1]) == testdata[2])

# tester for playLottery()
# the function is also a random function, we check the range
def playLotteryTester():
    list = [playLottery() for i in range(10)]
    for testdata in list:
        assert (testdata == -1 or testdata == 0 or testdata == 10 or testdata == 197 or testdata == 212535)



# tester for getDisparityMessage()
# the function is also a random function, we check the range
def getDisparityMessageTester():
    testdatas = [[[1, 2, 3], [1, 2], 1, "Decade " + str(1) + ": The high income group possesses " +\
        str(6 / 9 * 100) + "% of the community's wealth, while the low"\
        "income group possesses " + str(3 / 9 * 100) +\
        "% of the community's wealth."]
        , [[20, 40, 80], [10, 20], 5, "Decade " + str(5) + ": The high income group possesses " +\
        str((20 + 40 + 80) / (10 + 20 + 20 + 40 + 80) * 100) + "% of the community's wealth, while the low"\
        "income group possesses " + str((10 + 20)  / (10 + 20 + 20 + 40 + 80) * 100) +\
        "% of the community's wealth."]]

    for testdata in testdatas:
        assert(getDisparityMessage(testdata[0], testdata[1], testdata[2]) == testdata[3])

# tester for awardScholarship()
# the function is also a random function, we check the range
def awardScholarshipTester():
    testdatas = [[[1, 2, 3, 4, 5], 10]
                 , [[12, 43, 5, 2, 3], 100]]
    for testdata in testdatas:
        wealth1 = sum(testdata[0])
        awardScholarship(testdata[0], testdata[1])
        wealth2 = sum(testdata[0])
        assert(wealth1 == wealth2 - testdata[1])

def main():
    generateLotteryNumbersTester()
    countMatchesTester()
    playLotteryTester()
    getDisparityMessageTester()
    awardScholarshipTester()
    print("All test passed")

if __name__ == "__main__":
    main()