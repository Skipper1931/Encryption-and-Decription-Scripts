#Run with the Python Launcher for it to work

print('English to Pig Latin Translator. Type "quit" (without quotes) to quit. Make sure to only use letters!')

def translate() :
	pyg = 'ay'

	original = raw_input("Enter a word ")
	original = original.lower()

	#Quits the program as needed
	if original == "quit":
		quit = raw_input("Quit? (Y/N)")
		quit = quit.lower()
		quitConfirm(quit)
	
	#Makes sure word is a word and also not a curse
	elif len(original) > 0 and original.isalpha() and original != "fuck" and original != "shit" and original != "bitch" and original != "ass" and original != "damn" and original != "dick":
  		#Translates word
  		print("Your original word was: " + original)
  		first = original[0]
  		new_word = original + first + pyg
  		new_word = new_word[1:]
  		#Prints translated word
  		print("Your translated word is: " + new_word)
		translate()
	elif original == "quit()":
		print("Debug Quit")
		quit()
	else:
  		print("Your word was either not a word, or a curse! Try again!")
  		translate()

#Confirms that you want to quit
def quitConfirm(q):
	if q == "y":
		quit()
	elif q == "n":
		print("Your original word was: quit")
		print("Your translated word is: itquay")
		translate()
	else:
		print("LOL")
		translate()

translate()
