# Shang Xiao
# April 20, 2022
# CS 5001 Project 9
# Tickets.py

from asyncio import QueueEmpty
from Queue import Queue
import random

peopleNum = 1
peopleInQueue = 0

Peoples = []
file = open("People.txt", "r")
for i in file.readlines():
    Peoples.append(i[:-1])

q = Queue(200) # the maximum number of people is up to 200

for i in range(100):
    toJoin = random.randint(0, 2) # randomly choose 0 to 2 people join the queue
    print(str(toJoin) + " people joined the queue.")
    for j in range(toJoin):
        q.enqueue(peopleNum)
        peopleNum += 1
        peopleInQueue += 1
    if(q.end != q.start): # if the queue is not empty, then dequeue the front people
        peopleInQueue -= 1
        served = Peoples[q.dequeue() - 1]
        print("Customer " + str(served) + " is served!")
    else:
        print("Now queue is empty!")

print("Now there are " + str(peopleInQueue) + " people in queue.")
