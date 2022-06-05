# Project 6
# Lottery and Wealth Simulation
# Shang Xiao
# March 8, 2022

import random
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib


# ----------------- THE SIMULATION ----------------- #

def generateLotteryNumbers():
    """
    Returns a list of 5 random ints between 1 and 42, inclusive, with no
    duplicates.
    """
    # YOUR CODE HERE
    # Reference: https://www.w3schools.com/python/ref_random_sample.asp
    # this webpage introduced the random.sample() method within Python random. The syntax is 'random.sample(sequence, k)'
    # where 'sequence' can be any sequence such as lists, sets, ranges. In this case, list(range(1, 43))
    # where 'k' is the size of the returned list. In this case, 5
    return random.sample(list(range(1, 43)), 5)


def countMatches(my_list, lottery_list):
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    # YOUR CODE HERE
    # Reference: https://www.w3schools.com/python/ref_list_count.asp
    # count() is one of the list methods mentioned in the above webpage instructed by w3schools.com
    # count() comes very handy in this situation. Since we need to compare if one element in one list is the same
    # as another element in another list, we will use this list method. The syntax is 'list.count(value)'. In this case
    # we want to know if any element in my_list matches with any element in lottery_list, the value we are searching for
    # every time is 'i', thus, we use 'for' to loop through my_list and the counter will +=1 everytime when there is a
    # match between my_list and lottery_list
    cnt = 0
    for i in my_list:
        if lottery_list.count(i) > 0:
            cnt += 1
    return cnt


def playLottery():
    """
    Returns the reward after one lottery play.
    """
    # YOUR CODE HERE
    # as instructed, use 'generateLotteryNumbers()' and 'countMatches' as helper functions, we can get the number of
    # matches for two lists from the result of 'cnt', and we can then use 'if' statements to link each scenario to
    # its corresponding reward respectively

    # running generateLotteryNumbers() two times because one is for lottery, another one is for player
    my_list = generateLotteryNumbers()
    lottery_list = generateLotteryNumbers()

    # set variable cnt to get the number of matches and then compare
    cnt = countMatches(my_list, lottery_list)
    if cnt <= 1:
        return -1
    elif cnt == 2:
        return 0
    elif cnt == 3:
        return 10
    elif cnt == 4:
        return 197
    else:
        return 212534


def getDisparityMessage(highIncomeList, lowIncomeList, decade):
    """
    Returns a string that describes the percentages of wealth possessed by the
    higher income half and lower income half for any given year.
    Inputs: *highIncomeList: The list containing wealth values for the high
             income group.
            *lowIncomeList: The list containing wealth values for low income
             group.
            *decade: The current decade as an integer.
    """
    # YOUR CODE HERE
    # we are instructed to write two equations that calculates the percentage of wealth possessed by two groups
    # the first example given is 50% and 50%, this is because (2+3+4+5+6) / ((2+3+4+5+6) + (6+5+4+3+2)) * 100 = 50%
    # the third example given is 79% and 21%, this is because (4+10+2+5+8) / ((4+10+2+5+8) + (2+7+12)) * 100 = 79%
    # and (2+7+12) / ((4+10+2+5+8) + (2+7+12)) * 100 = 21%, thus
    # percent of low income
    lowIncomePercent = sum(lowIncomeList) /  (sum(highIncomeList) + sum(lowIncomeList)) * 100
    # percent of high income
    highIncomePercent = sum(highIncomeList) /  (sum(highIncomeList) + sum(lowIncomeList)) * 100

    message = "Decade " + str(decade) + ": The high income group possesses " +\
        str(highIncomePercent) + "% of the community's wealth, while the low"\
        "income group possesses " + str(lowIncomePercent) +\
        "% of the community's wealth."

    return message


def simLottery(incomeList, numPlayers):
    """
    Simulates lottery play for a number of players from a given income group.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            *numPlayers: The number of players who will play the lottery.
    """
    for i in range(numPlayers):
        # YOUR CODE HERE
        # select a person in the list and simulate play a round of Lottery
        # add the result of this Lottery to the person's sum of wealth
        incomeList[random.randint(0, len(incomeList) - 1)] += playLottery()
        pass

def awardScholarship(incomeList, awardTotal):
    """
    Redistributes funds from the lottery in the form of a $1 scholarship.
    Inputs: *incomeList: The list containing wealth values for the given
             income group.
            *awardTotal: The total amount of lottery funds to be rewarded
             to members of this income group.
    """
    for i in range(awardTotal):
        # YOUR CODE HERE
        # simulate the distribution of scholarship
        # select some student, each of them add 1 to their sum of wealth
        incomeList[random.randint(0, len(incomeList) - 1)] += 1
        pass


def simCommunity(years, communitySize):
    """
    Simulates the movement of money between high income and low income
    communities via the Georgia lottery and scholarship system over several
    years. Half of the community is from low income backgrounds, and half from
    high income backgrounds. The resulting wealth disparity is printed as a
    message and displayed as a scatter plot indicating overall wealth per
    person per year.
    Inputs: *years: The number of years the simulation should be run.
            *communitySize: The number of people in the community.
    """

    # ---- PART 1: Populate Wealth Lists
    # Fill highIncomeList and lowIncomeList with starting wealth values

    # half is high income, the other half is low income
    # initiate their money with 100 and 99
    highIncomeList = [100 for i in range(communitySize // 2)]
    lowIncomeList = [99 for i in range(communitySize - communitySize // 2)]

    # ---- PART 2: Populate Record Lists
    # Fill highIncomeRecord and lowIncomeRecord with the starting ("year 0")
    # values from highIncomeList and lowIncomeList

    # using copy() method to made a copy and preserve them into record list
    # if we don't use copy() method, when the origin list change, the list in record will also change
    highIncomeRecord = [highIncomeList.copy()]
    lowIncomeRecord = [lowIncomeList.copy()]

    # simulation loop
    for i in range(years):

        # ---- PART 3: Play the Lottery
        # Use the simLottery() function to simulate community
        # wealth interactions


        # the fund before play - fund after play is the scholarship
        fund = sum(highIncomeList) + sum(lowIncomeList)
        simLottery(lowIncomeList, int(len(lowIncomeList) * 0.6))
        simLottery(highIncomeList, int(len(highIncomeRecord) * 0.4))
        fund = fund - (sum(highIncomeList) + sum(lowIncomeList))

        # ---- PART 4: Award Scholarships
        # Use the awardScholarship() function to redistribute lottery funds
        # as scholarships

        # distribute scholarship to high and low income people
        awardScholarship(highIncomeList, int(fund * 0.7))
        awardScholarship(lowIncomeList, int(fund * 0.3))

        # ---- PART 5: Update Record Lists
        # Update the income records every year

        # use copy() method like before
        highIncomeRecord.append(highIncomeList.copy())
        lowIncomeRecord.append(lowIncomeList.copy())
        if i % 10 == 0:
            # ---- PART 6: Display Wealth Distribution
            # Use getDisparityMessage() to display the wealth distribution
            # every decade

            # each 10 years, we print the change of high income and low income
            # it is i // 10 decades
            print(getDisparityMessage(highIncomeList, lowIncomeList, i // 10))
            pass
    # ---- PART 7: Visualize the Simulation
    # Uncomment the next line to plot the simulation
    plotSim(highIncomeRecord, lowIncomeRecord)


# ----------------- HELPER FUNCTIONS ----------------- #
# These functions are provided for you to use.
# You do not need to change them, but feel free to explore what they do.

def plotSim(highIncomeRecord, lowIncomeRecord):
    """
    Helper function for simCommunity() to generate a scatterplot displaying
    the wealth of each person in the simulation over 8 decades. High income
    values are plotted in red. Low income values are plotted in blue.
    Inputs: *highIncomeRecord: A list of all high income wealth lists
            from each year.
            *lowIncomeRecord: A list of all low income wealth lists
             from each year.
    """
    x = np.arange(len(highIncomeRecord))

    # plot wealth records
    plotWealthRecord(x, highIncomeRecord, '#882255', '.')
    plotWealthRecord(x, lowIncomeRecord, '#44AA99', '*')

    # plot labels/legend
    plt.xlabel("Year")
    plt.ylabel("Wealth Value")
    magenta_patch = mpatches.Patch(color='#882255', label='High Income')
    teal_patch = mpatches.Patch(color='#44AA99', label='Low Income')
    plt.legend(handles=[magenta_patch, teal_patch])

    # display the plot
    plt.show()


def plotWealthRecord(x, record, markerColor, markerShape):
    """
    Helper function for plotSim(). Plots each individual wealth group.
    Inputs: *x: List of x-axis values.
            *record: The income record to be plotted.
            *markerColor: String defining the color of markers.
            *markerShape: String defining marker shape.
    """
    for i in range(len(record[0])):
        plotData = []
        for j in range(len(record)):
            plotData += [record[j][i]]
        plt.scatter(x, plotData, color=markerColor, marker=markerShape)


def simManyPlays(n):
    """
    Function to graph the total winnings of a player who plays the lottery
    n times.
    Inputs: *n: The number of times the player enters the lottery.
    """
    winnings = []
    reward = 0
    for i in range(n):
        reward += playLottery()
        winnings.append(reward)
    plt.xlabel("Number of Lottery Plays")
    plt.ylabel("Winnings")
    plt.plot(winnings)
    plt.legend()
    plt.show()

# ----------------- MAIN FUNCTION ----------------- #


def main():
    # Simulate 1000 plays by one person and plot the winnings.
    simManyPlays(1000)

    # Simulate a community playing Lottery 5 with 30 people for 80 years.
    simCommunity(80, 30)

if __name__ == "__main__":
    main()
