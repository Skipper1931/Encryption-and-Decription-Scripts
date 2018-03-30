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

xbound = input("What do you want the boundary to be for the x axis? (Enter 'd' to use the default)")
ybound = input("What do you want the boundary to be for the y axis? (Enter 'd' to use the default)")

if xbound == "d":
    xbound = 300
else:
    xbound = int(xbound)
if ybound == "d":
    ybound = 250
else:
    ybound = int(ybound)


# staring vars
steps = randint(randMin,randMax)
step = 1
stps = str(steps)
print("There will be " + stps + " steps.")

# loop function thing because im too lazy to just use a loop (I like functions :P)
def loop():

    # global variables because i always somehow endup using these dang things (I like 'em tho)
    global steps
    global step
    global randMin
    global randMax
    global stps
    global xbound
    global ybound

    # prevents turtle from moving off screen
    x = xcor()
    y = ycor()
    x = int(x)
    y = int(y)
    xoff = xbound - 1
    yoff = ybound - 1
    
    if x >= xbound:
        setx(xoff)
    elif x <= 0 - xbound:
        setx(0 - xoff)

    if y >= ybound:
        sety(yoff)
    elif y <= 0 - ybound:
        sety(0 - yoff)
    
    # meat
    if step != steps + 1:
        # RNG
        operation = randint(1,2)
        opNum = randint(randMin,randMax)
        stp = str(step)

        # sets up screen
        screensize(2000,1500)
        
        # writes turtle to screen
        if operation == 1:
            print("Step " + stp + "/" + stps + ": Left")
            if opNum > 360:
                left(randint(randMin,359))
            else:
                left(opNum)
            forward(80)
            step = step + 1
            operation = 0
            opNum = 0
            loop()
        elif operation == 2:
            print("Step " + stp + "/" + stps + ": Right")
            if opNum > 360:
                right(randint(randMin,359))
            else:
                right(opNum)
            forward(80)
            step = step + 1
            operation = 0
            opNum = 0
            loop()
    else:
        import thank

loop()
