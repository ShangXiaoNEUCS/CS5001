# Shang Xiao
# April 6, 2022
# CS 5001 Project 8
# File which will hold the implementation of Scoop

from math import pi

class Scoop:
    '''Class Scoop
       Attributes: radiuscl
       Methods: volume'''

    def __init__(self, radius):
        '''
        Constructor - creates a new instance of Scoop
        Parameters -
           self - the current object
           radius - the radius of the scoop
        '''
        self.radius = radius
        pass
    
    def volume(self):
        ''' Method - calculate the volume of the scoop
        Parameters:
           self - the current object
        '''
        return 4 / 3 * pi * self.radius ** 3
