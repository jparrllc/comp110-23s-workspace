"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730479825"
word: str = input("Enter a 5-character word:")
if (len(word) != 5):
    print ("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character:")
if (len(letter) != 1):
    print ("Error: Character must be a single character")
    exit()
print("Searching for " + letter + " in " + word)

matching_characters: int = 0 
if (letter == word [0]):
    print (letter + " found in index 0")
    matching_characters = 1 + matching_characters
if (letter == word [1]):
    print (letter + " found in index 1")
    matching_characters = 1 + matching_characters 
if (letter == word [2]):
    print (letter +  " found at index 2")
    matching_characters = 1 + matching_characters
if (letter == word [3]):
    print (letter + " found at index 3")
    matching_characters = 1 + matching_characters
if (letter == word [4]):
    print (letter + " found at index 4")
    matching_characters = 1 + matching_characters

if (matching_characters == 0 ):
    print ("No instances of " + letter + " found in " + word)

if (matching_characters == 1):
    print(str(matching_characters) + " instance of "  + letter + " found in " + word)

else: 
    print(str(matching_characters) + " instances of "  + letter + " found in " + word)