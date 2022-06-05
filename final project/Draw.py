# CS 5001
# Final Project
# Guitar Diagram for Beginners Program
# Shang Xiao
# May 2, 2022
# this file links the two classes Chord and FretboardPainter

from Chord import Chord
from FretboardPainter import FretboardPainter

fbp = FretboardPainter()
nowChord = Chord()

# read key and level from file
file = open("key.txt", "r")
s = file.readline().split()

# get chord by key and level
nowChord.load(s[0], int(s[1]))

# show picture
fbp.showChord(nowChord)