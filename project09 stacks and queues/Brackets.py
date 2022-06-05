# Shang Xiao
# April 20, 2022
# CS 5001 Project 9
# Brackets.py

from Stack import Stack
def verify(s):
    stk = Stack(len(s))

    for i in range(len(s)):
        if(s[i] == ')' or s[i] == '}' or s[i] == ']' or s[i] == '>'): # when current character is right bracket
            if(stk.end == 0): # when current stack is empty
                return False    
            top = stk.pop() # get top of stack
            if(s[i] == ')' and top != '(' or s[i] == '}' and top != '{' or s[i] == ']' and top != '[' or s[i] == '>' and top != '<'):
                return False # return false if top can't match current right bracket
        else:
            stk.push(s[i])
    
    return stk.end == 0 # valid when stack is empty

