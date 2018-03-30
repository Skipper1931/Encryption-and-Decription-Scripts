# Thanks for using my script thinger

# initial user input
yn = input("Thank you for using one of my scripts! Would you like to use another? (y or n)")
yn = yn.lower()

# meat
def thank():
    script = input("Type 'pig' to go to my pig latin translator, 'draw' to go to my random drawer, and 'thanks' to go to my thank you writer")
    script = script.lower()
    if script == "pig":
        import piglatin
    elif script == "draw":
        import randomDraw
    elif script == "thanks":
        import thankLetter
    else:
        print("You did not put in the right keyword! Try again!")
        thank()

if yn == "y":
    thank()

    
