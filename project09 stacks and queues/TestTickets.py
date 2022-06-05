# Shang Xiao
# April 20, 2022
# CS 5001 Project 9
# TestTickets.py

from random import randint

file = open("People.txt", "w")
# generate 200 people to test the tickets application
def getRandomString(len):
    ret = ""
    for i in range(len):
        ret += chr(ord('a') + randint(0, 25))
    return ret

for i in range(200):
    file.writelines(getRandomString(10) + "\n")