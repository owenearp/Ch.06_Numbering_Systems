word = input("Enter a word to encrypt: ")
encrypted=""
for letter in word:
    i = ord(letter) + 5
    newletter = chr(i)
    encrypted += newletter
print(encrypted)
print(chr(33))

