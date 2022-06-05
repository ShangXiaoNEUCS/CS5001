# Shang Xiao
# April 6, 2022
# CS 5001 Project 8
# File which will hold the implementation of Carton

from math import pi #this gives you pi
import Scoop

class Carton:
    ''' Class: Carton
        Attributes: contains
        Methods: hasEnoughFor, remove'''
    
    def __init__(self, radius, height):
        ''' Constructor
            Parameters:
                self
                radius - radius of a carton
                height - height of a carton'''
        self.contains = radius ** 2 * pi * height
        pass

    def hasEnoughFor(self, scoop):
        ''' hasEnoughFor
            Parameters:
                scoop - the Scoop to be used on the Carton
            Return:
                whether or not the Carton contains enough to make a Scoop'''
        return self.contains >= scoop.volume()

    def remove(self, scoop):
        ''' remove
            Parameters:
                scoop - the Scoop to be used on the Carton
        '''
        self.contains -= scoop.volume()
        pass