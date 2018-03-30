# Random line drawer
# By Skipper1931

# imports libs
from random import *
from turtle import *

# gets user input
randMin = input("Enter the minimum integer for the random number generator ")
randMax = input("Enter the maximum integer for the random number generator ")
randMin = int(randMin)
randMax = int(randMax)

# staring vars
steps = randint(randMin,randMax)
step = 1
stepPrint = str(steps)
print("There will be " + stepPrint + " steps.")

# while loop function because im too lazy to just use a loop (I like functions :P)
def loop():

    # global variables because i always somehow endup using these dang things (I like 'em tho)
    global steps
    global step
    global randMin
    global randMax

    # meat
    if step != steps + 1:
	    operation = randint(1,2)
	    opNum = randint(randMin,randMax)
	    opNum = int(opNum)
	    stp = str(step)
	    if operation == 1:
		    print("Step " + stp + ": Left")
		    left(opNum)
		    forward(opNum)
		    step = step + 1
		    operation = 0
		    loop()
	    elif operation == 2:
		    print("Step " + stp + ": Right")
		    right(opNum)
		    forward(opNum)
		    step = step + 1
		    operation = 0
		    loop()

loop()
