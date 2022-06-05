# Shang Xiao
# April 20, 2022
# CS 5001 Project 9
# Stack.py

''' Align Online
    CS5001
    Sample code -- example of implementing the Stack ADT
'''

class Stack:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our stack
        '''
        self.data = [0] * size
        self.end = 0

    def push(self, item):
        ''' push -- adds something to the top of the stack
        Parameters:
           self -- the current object
           item -- the item to add to the stack
        Returns nothing
        '''
        if self.end >= len(self.data):
            print("Full!")
            return
        self.data[self.end] = item
        self.end += 1

    def pop(self):
        ''' pop -- removes something from the top of the stack
        Parameters:
           self -- the current object
        Returns the top element after removing it from the stack
        '''
        if self.end <= 0:
            print("Empty!")
            return
        self.end -= 1
        return self.data[self.end]

    def dump(self):
        ''' dump -- debugging method for the stack
        Parameters:
           self -- the current object
        '''
        for i in range(self.end - 1, -1, -1):
            print(self.data[i])


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

def main():
    s = input("Please input a string of bracket: ")

    if(verify(s)):
        print("Valid!")
    else:
        print("Invalid!")

if __name__ == "__main__":
    main()
