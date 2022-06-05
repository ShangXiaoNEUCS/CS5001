# Shang Xiao
# April 20, 2022
# CS 5001 Project 9
# TestBrackets.py

import Brackets

# possible combinations from the user
s = ["<><>", "<[]>{<>}", "{}<}{>", "}{", ""]
ans = [True, True, False, False, True]

#check if the verify(s) function works
for c, b in zip(s, ans):
    if(Brackets.verify(c) == b):
        print("Correct")
    else:
        print("Wrong")

print("All test passed!")