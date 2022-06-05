# CS 5001
# Final Project
# Guitar Diagram for Beginners Program
# Shang Xiao
# May 2, 2022
# main function contains user interface and implements the algorithm

import os

while(True):
    print("Please input the key and level sperated by a whitespace: ")
    ss = input()
    s = ss.split()
    key, level = s[0], int(s[1])
    # check whether key or level is valid
    if(key not in ['A', 'B', 'C', 'D', 'E', 'F', 'G'] or level not in [1, 2, 3, 4, 5, 6, 7]):
        print("Invalid input!")
        continue
    
    # write key and level to file
    file = open("key.txt", "w")
    file.write(ss)
    file.close()
    os.system("python Draw.py")

    # ask user whether need to convert the current chord to another key
    while(True):
        temp = input("Do you want to convert the current chord to another key? (Y/N)")
        if(temp == 'N'):
            break
        newkey = input("Which key do you want to convert the current chord to? (C/D/E/F/G/A/B)")
        if(newkey not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']):
            print("Invalid input!")
            continue
        if(newkey == key):
            print("Chord is the same!")
        else:
            file = open("key.txt", "w")
            file.write(newkey + " " + str(level))
            file.close()
            os.system("python Draw.py")
    