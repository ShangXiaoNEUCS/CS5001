# CS 5001
# Final Project
# Guitar Diagram for Beginners Program
# Shang Xiao
# May 2, 2022
# class FretboardPainter prints out chords

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from Chord import Chord

fig, ax = plt.subplots(figsize=(20,6))

class FretboardPainter:
    def __init__(self):
        pass


    '''
    First clean the plt, and then draw the strings of a guitar
    '''
    def init(self):
        plt.cla()
        for i in range(1,7):
            ax.plot([i for a in range(22)])
        # Plotting Frets
        for i in range(1,21):
            # decorates the twelve fret with a gray and thick fret
            if i == 12:
                ax.axvline(x=i, color='gray', linewidth=3.5)
                continue
            # trace a vertical line (a fret)
            ax.axvline(x=i, color='black', linewidth=0.5)
        ax.set_axisbelow(True)
        
        # setting height and width of displayed guitar
        ax.set_xlim([0, 21])
        ax.set_ylim([1, 6])
        # setting color of the background using argument night
        ax.set_facecolor('white')
        plt.yticks(np.arange(1,7), ['E', 'A', 'D', 'G', 'B', 'E'])
        plt.xticks(np.arange(21)+0.5, np.arange(1,22))


    '''
    Add the positions of the fingers in the chord to the picture one by one,
    and show the picture
    '''
    def showChord(self, chord):
        self.init()
        for i in chord.fingerPositions:
            if(len(i) == 3):
                # add a circle to plt.
                offset = 0
                if(i[0] == 1): offset = 0.1
                if(i[0] == 6): offset = -0.1
                p = mpatches.Circle((i[1] - 0.5, i[0] + offset), 0.2)
                ax.add_patch(p)
                ax.annotate(i[2], (i[1] - 0.5, i[0] + offset), color='w', weight='bold', 
                            fontsize=12, ha='center', va='center')
            else: # Barre Chord
                # add a rectangle to plt.
                p = mpatches.Rectangle((i[2] - 0.6, i[0]), 0.2, i[1] - i[0])
                ax.add_patch(p)
                ax.annotate(i[3], (i[2] - 0.5, (i[0] + i[1]) / 2), color='w', weight='bold', 
                            fontsize=12, ha='center', va='center')
        plt.show()