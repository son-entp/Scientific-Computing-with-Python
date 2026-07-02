text = 'Hello world'
#print(text) #just prints a variable
#print(text[8]) prints a letter whis on position 8
#print(len(text)) prints lenght of the string
#print(type(text))
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index]
print(shifted)