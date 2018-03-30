# Skipper1931's Pyg Latin Translator
# Run on CodeSkulpter.org for best effect!
# Have fun! :D

# opening text
print('Translator Output Log:')

# defines global variables in order to prevent undefined var error in functions
lastword = 'empty'
p3 = 'empty'
tutorial = 0
word = 1

# asks if you want to do the tutorial
def tutConf():
    global tutorial
    p0 = input("Do you want to do the tutorial? (Y/N)")
    p0 = p0.lower()
    if p0 == 'y':
        tutorial()
    else:
        tutorial = 1
        translate()

# tutorial function
def tutorial() :
    global lastword
    global p3
    pyg = 'ay'
    cancel = 0
    p1 = input("Welcome to Skipper1931's Pyg (pig?) Latin translator! Type in any word to start the tutorial!")
    if p1 == 'none':
        p2 = input("Actually, hitting 'cancel,' due to some quirks in CodeSkulpter, will output 'None.' Either way, good job! Type in another word to translate it!")
        cancel = 1
    else:
        p2 = input("Good job! Type in another word to translate it!")
    p2 = p2.lower()
    if p2 == 'none' and cancel == 0:
        first = p2[0]
        new_word = p2 + first + pyg
        new_word = new_word[1:]
        lastword = new_word
        p3 = input("Actually, hitting 'cancel,' due to some quirks in CodeSkulpter, will output 'None.' Either way, good job! Your translated word is " + lastword + ". Just a reminder, typing quit will start the quit process! Have fun!")
        translate()
    elif p2 == 'none' and cancel == 1:
        first = p2[0]
        new_word = p2 + first + pyg
        new_word = new_word[1:]
        lastword = new_word
        p3 = input("Seriously? You did it again? Oh yeah, by the way, type quit to quit.")
        translate()
    else:
        first = p2[0]
        new_word = p2 + first + pyg
        new_word = new_word[1:]
        lastword = new_word
        p3 = input("Good job! Your translated word is " + lastword + ". Just a reminder, typing quit will start the quit process. One last thing, if you hit 'cancel,' due to some quirks in CodeSkulpter, will cause the program to output 'None'. Have fun!")
        translate()

# main translator function
def translate() :
    pyg = 'ay'
    global word
    global tutorial
    global lastword
    global p3
    # input
    if tutorial == 1:
        original = input("Enter a word. Your last word was " + lastword + ".")
    else:
        original = p3
        tutorial = 1
    original = original.lower()

    # Quits the program as needed
    if original == "quit":
        quit = input("Quit? (Y/N)")
        quit = quit.lower()
        quitConfirm(quit)
    
    # Makes sure word is a word and also not a curse
    elif len(original) > 0 and original != "fuck" and original != "shit" and original != "bitch" and original != "ass" and original != "damn" and original != "dick":
        # Translates word
        first = original[0]
        new_word = original + first + pyg
        new_word = new_word[1:]
        lastword = new_word
        # Prints log
        word = str(word)
        print(word + ". original: " + original)
        print(word + ". translated: " + new_word)
        word = int(word)
        word = word + 1
        translate()
    else:
        # If none of the above apply
        lastword = 'either not a word, or a curse! Try again!'
        word = str(word)
        print(word + ". original either was not a word, or a curse.")
        word = int(word)
        word = word + 1
        translate()

# quit confirmation function
def quitConfirm(q):
    global word
    global lastword
    if q == "y":
        import thank
    else:
        word = str(word)
        print(word + ". original: quit")
        print(word + ". translated: itquay")
        word = int(word)
        word = word + 1
        lastword = 'itquay'
        translate()
        
tutConf()
