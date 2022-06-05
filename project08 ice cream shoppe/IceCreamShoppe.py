# Shang Xiao
# April 6, 2022
# CS 5001 Project 8
# File which will implement the IceCreamShoppe class

from Carton import *
from Scoop import *

class IceCreamShoppe:
    '''Class IceCreamShoppe
        Attributes: carton_radius, carton_height, cartons_used
        Methods: serve, cartonsUsed'''

    def __init__(self, carton_radius, carton_height):
        ''' Constructor
        Parameters: carton_radius, carton_height - dimensions for a carton
        Return: nothing'''
        self.carton_radius = carton_radius
        self.carton_height = carton_height
        self.cartons_used = 1
        self.current_carton = Carton(carton_radius, carton_height)
        pass

    def serve(self, numScoops, scooper):
        ''' serve method
        Parameters: numScoops - number of scoops wanted; 
            scooper - the specific Scoop to use
        Return: nothing'''
        for i in range(numScoops):
            if(not self.current_carton.hasEnoughFor(scooper)):
                self.current_carton = Carton(self.carton_radius, self.carton_height)
                self.cartons_used += 1
            self.current_carton.remove(scooper)
        pass

    def cartonsUsed(self):
        ''' cartonsUsed method
        Parameters: none
        Return: the number of cartons used so far in the Shoppe'''
        return self.cartons_used