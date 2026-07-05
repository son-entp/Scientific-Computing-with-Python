text = 'Hello world'
#print(text) #just prints a variable
#print(text[8]) prints a letter whis on position 8
#print(len(text)) prints lenght of the string
#print(type(text))
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    index = alphabet.find(char)    
    new_index = index + shift
    encrypted_text = alphabet[new_index]
    print('char:', char, 'encrypted_text:', encrypted_text)