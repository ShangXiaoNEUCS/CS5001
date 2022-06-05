# CS 5001
# Final Project
# Guitar Diagram for Beginners Program
# Shang Xiao
# May 2, 2022
# this file is for class Chord and its corresponding chords

whole_notes = ['C','C#','D','D#','E','F',
               'F#','G','G#','A','A#','B']*2

interval = [0, 2, 4, 5, 7, 9, 7]

class Chord:
    def __init__(self) -> None:
        self.fingerPositions = []
        pass

    '''
    Calculate the corresponding chord by key and level, and then read the position of the finger of this chord from the file
    '''
    def load(self, key, level): # load fingerPositions by key and level
        self.fingerPositions = []
        ind = whole_notes.index(key)
        to_load = interval[level - 1]
        s = whole_notes[ind + to_load]
        # special chord (does not fit the pattern)
        if(level in [2, 3, 6] or key == 'E' and level == 5):
            s += 'm'
        if(level == 7):
            s += '7'
        if(key == 'F' and level == 4):
            s = 'bB'
        print(s)
        # open file to get finger position information
        with open("chords/" + s + ".txt", "r") as file:
            fingerPositionStr = file.readlines()
            for i in fingerPositionStr:
                tmp = i.split()
                if(len(tmp) == 3):
                    self.fingerPositions.append((int(tmp[0]), int(tmp[1]), tmp[2]))
                if(len(tmp) == 4): # Bar Chord (such as F)
                    self.fingerPositions.append((int(tmp[0]), int(tmp[1]), int(tmp[2]), tmp[3]))
