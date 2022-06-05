# CS 5001
# Final Project
# Guitar Diagram for Beginners Program
# Shang Xiao
# May 2, 2022
# testing file that checks each chord diagram txt document

import Chord
key = 'CDEFGAB'

chord = Chord.Chord()

for i in key:
    for j in range(7):
        print(i, j + 1)
        chord.load(i, j + 1)
        print(chord.fingerPositions)