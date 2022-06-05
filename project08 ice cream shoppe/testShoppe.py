# Shang Xiao
# April 6, 2022
# CS 5001 Project 8
# testShoppe

from Carton import *
from Scoop import *
from IceCreamShoppe import *

iceCreamShoppe = IceCreamShoppe(10, 10)
iceCreamShoppe.serve(10, Scoop(10))

print(iceCreamShoppe.cartonsUsed())