# Thank You Writer-maker thinger
# By Skipper1931


# main func.
def thank():
    
    # Get's user input
    name = input("What is your name?")
    event = input("What type of event did you host? (e.g. Bar Mitzvah, Birthday Party, Wedding, etc.)")
    first = input("What is the recipiant of this letter's first name? (e.g. John)") 
    last = input("What is the recipiant of this letter's last name? (e.g. Smith)")
    adult = input("Is this person an adult? (y or n)")
    adult = adult.lower()
    if adult == "y":
        gender = input("What is the recipiant's gender? (f or m)")
        gender = gender.lower()
        friend = input("Are you friends with this person? (y or n)")
        friend = friend.lower()
        if gender == "f":
            married = input("Is the recipiant married? (y or n)")
            married = married.lower()
        else:
            married = " "
    else:
        gender = " "
        friend = " "

    print(" ")
    # Figures out greeting
    if friend == "y" or adult == "n":
        print("Dear " + first + ",")
    elif friend == "n" and gender == "m" and adult == "y":
        print("Dear Mr. " + last + ",")
    elif friend != "y" and gender == "f" and married == "y" and adult == "y":
            print("Dear Mrs. " + last + ",")
    elif friend != "y" and gender == "f" and married == "n" and adult == "y":
            print("Dear Ms. " + last + ",")              
    
    # Prints rest of message              
    print(" ")   
    print("Thank you so much for coming to my " + event + "! I had so much fun with you! Thank you so much for the generous gift!")  
    print(" ")
    print("Sincerely,")
    print(name)
    print(" ")
    import thank
                  
thank()
