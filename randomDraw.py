# Random line drawer
# By Skipper1931

# imports libs
from random import *
from turtle import *
from datetime import *
from tkinter import *

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
bounces = 0
print("There will be {} steps.".format(steps))
detailLog = " "

# loop
while step != steps + 1:
    
    # prevents turtle from moving off screen
    x = xcor()
    y = ycor()
    x = int(x)
    y = int(y)
    xoff = xbound - 1
    yoff = ybound - 1
    
    if x >= xbound:
        setx(xoff)
        bounces = bounces + 1
    elif x <= 0 - xbound:
        setx(0 - xoff)
        bounces = bounces + 1

    if y >= ybound:
        sety(yoff)
        bounces = bounces + 1
    elif y <= 0 - ybound:
        sety(0 - yoff)
        bounces = bounces + 1
    
    # meat
    if step != steps + 1:
        # RNG
        operation = randint(1,2)
        opNum = randint(randMin,randMax)
 
        # sets up screen
        screensize(2000,1500)
        
        # writes turtle to screen
        if operation == 1:
            print("Step {}/{}: Left. {} Bounces".format(step,steps,bounces))
            detailPre = "Step {}/{}: Left. {} Bounces".format(step,steps,bounces)
            if opNum > 360:
                left(randint(randMin,359))
            else:
                left(opNum)
            forward(80)
            step = step + 1
            operation = 0
            opNum = 0
        elif operation == 2:
            print("Step {}/{}: Right. {} Bounces".format(step,steps,bounces))
            detailPre = "Step {}/{}: Right. {} Bounces".format(step,steps,bounces)
            if opNum > 360:
                right(randint(randMin,359))
            else:
                right(opNum)
            forward(80)
            step = step + 1
            operation = 0
            opNum = 0
        detailLog = "{}\n{}".format(detailLog,detailPre)
# Logs Stuff
output = getscreen()
user = input("Would you like to save a more detailed log? (y or n)")
user = user.lower()

if step == steps + 1 and user != "y":
    date = datetime.now()
    log = open("bounces.log","a+")
    log.write("\n[{}] Bounces: {} Steps: {}".format(date.strftime("%Y-%m-%d %H:%M:%S"),bounces,steps))
    log.close()
    output.getcanvas().postscript(file="randomDrawOutput.eps")
    import thank
elif step == steps + 1 and user == "y":
    date = datetime.now()
    log = open("{}.log".format(date.strftime("%Y-%m-%d %H:%M:%S")),"a+")
    log.write("# Log for {}\n{}".format(date.strftime("%Y-%m-%d %H:%M:%S"),detailLog))
    log.close()
    log = open("bounces.log","a+")
    log.write("\n[{}] Bounces: {} Steps: {}".format(date.strftime("%Y-%m-%d %H:%M:%S"),bounces,steps))
    log.close()
    output.getcanvas().postscript(file="randomDrawOutput.eps")
    import thank
