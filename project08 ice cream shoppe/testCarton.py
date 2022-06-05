# Shang Xiao
# April 6, 2022
# CS 5001 Project 8
# testCarton

from Carton import *
from Scoop import *

carton = Carton(5, 10)
scoop = Scoop(5)

print(carton.contains)
print(carton.hasEnoughFor(scoop))
