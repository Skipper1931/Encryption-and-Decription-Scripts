# Random draw-er
# By Skipper1931

# imports libs.
from random import *
from turtle import *

# gets user input
randMin = input("Put in the minimum integer for the random number generator ")
randMax = input("Put in the minimum integer for the random number generator ")

# staring vars
steps = randint(randMin,randMax)
step = 0
print steps

# while loop function because im too lazy to just use a loop (I like functions :P)
def loop():
	
	# global variables because i always somehow endup using these dang things (I like 'em tho)
	global steps
	global step
	global randMin
	global randMax

	# meat
	if step != steps:
		operation = randint(0,3)
		opNum = randint(randMin,randMax)
		print opNum
		if operation == 1 and step != steps:
			left(opNum)
			forward(opNum)
			end()
		if operation == 2 and step != steps:
			right(opNum)
			forward(opNum)
			end()
		
# actual useful func. here bois
def end():
	
	# global var
	global step

	step = step + 1
	loop()