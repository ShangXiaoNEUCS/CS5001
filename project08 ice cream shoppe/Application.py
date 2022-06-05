# Shang Xiao
# April 6, 2022
# CS 5001 Project 8
# File which will hold the main function for the IceCreamShoppe project

import IceCreamShoppe
import Scoop

def main():
    # create scooper1 and scooper2
    scooper1 = Scoop.Scoop(float(input("What is the radius of your first scooper?")))
    scooper2 = Scoop.Scoop(float(input("What is the radius of your second scooper?")))

    # create iceCreamShoppe
    iceCreamShoppe = IceCreamShoppe.IceCreamShoppe(float(input("What is the radius of your carton?")), float(input("What is the height of your carton?")))

    # loop
    while(True):
        if(int(input("Would you like more ice cream? (Enter 1 for yes and 0 for no)")) == 0):
            # user does not want more, and program ends.
            print(f"You used {iceCreamShoppe.cartonsUsed()} cartons of ice cream.")
            break

        # ask the user for number of scooper1 and the number of scooper2
        numScooper1 = int(input(f"How many {scooper1.radius} scoops would you like?"))
        numScooper2 = int(input(f"How many {scooper2.radius} scoops would you like?"))

        iceCreamShoppe.serve(numScooper1, scooper1)
        iceCreamShoppe.serve(numScooper2, scooper2)
    pass

if __name__ == "__main__":
    main()