#Run with the Python Launcher for it to work

pyg = 'ay'

original = raw_input("Enter a word ")

#Makes sure word is a word
if len(original) > 0 and original.isalpha():
  #Translates word
  print("Your original word is: " + original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:]
else:
  print("null")
#Prints translated word
print("Your translated word is: " + new_word)
    
    
