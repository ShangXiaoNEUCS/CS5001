# Shang Xiao
# Jan 26, 2022
# CS5001
# Algorithm 3 for Lab 2

def s():

    # ask user to input three variable, the day, month, and year, in number form, as requested
    day = int(input("Please enter a date in number form, for example, 25th is 25"))
    month = int(input("Please enter a month in number form, for example, March is 3"))
    year = int(input("Please enter a year in number form, for example, 2022 is 2022"))

    # based on "https://www.almanac.com/content/first-day-seasons",
    # winter is from Dec 21 to Mar 19, we first make sure Jan - Mar is covered
    if month>=1 and month<=3:
        season = "Winter"
    # spring is from Mar 20 to Jun 20, we first make sure Apr - Jun is covered
    elif month>=4 and month<=6:
        season = "Spring"
    # summer is from Jun 21 to Sep 21, we first make sure Jul - Sep is covered
    elif month>=7 and month<=9:
        season = "Summer"
    # fall is from Sep 22 to Dec 20, we first make tO STAsure Oct - Dec is covered
    else:
        season = "Fall"

    # we have not cover spring days in Mar, we then make sure spring days in Mar is covered
    if month==3 and day>19:
        season = "Spring"
    # we have not cover summer days in Jun, we then make sure summer days in Jun is covered
    elif month==6 and day>20:
        season = "Summer"
    # we have not cover fall days in Sep, we then make sure fall days in Sep is covered
    elif month==9 and day>21:
        season = "Fall"
    # we have not cover winter days in Dec, we then make sure winter days in Dec is covered
    elif month==12 and day>20:
        season = "Winter"

    # the algorithm now is complete and will run from the top to the bottom, we make sure the final output is
    # returned back to the user correctly
    in


s()
