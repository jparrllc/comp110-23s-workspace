"""EX02 One-Shot Wordle."""
__author__ = "730479825"

secret_word = str("python")
secret_length: int = len(secret_word)
guess: str = input(f"What is your {secret_length}-letter guess? ")
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
ind: int = 0
emoji_result: str = " "
anywhere_else: bool = False 
while playing:  # "playing" acts as a on/off switch for the while statement, since playing is false, if it becomes true you exit the loop
    if (guess == secret_word):  # this if statemnt tells the program what to do when the guess is correct/when the input is equal to the guess  
        while ind < len(secret_word):  # ind keeps track of which letter your on, since the letters are the same it assigns a green box and then moves to the next letter
            if guess[ind] == secret_word[ind]:
                emoji_result = emoji_result + GREEN_BOX
            ind = ind + 1
        print(emoji_result)
        print("Woo! You got it! ")
        playing = False  # loop is exited
    if (len(guess)) != secret_length:  # this if statement is for when the length of the guess is not equal to the length of the correct word 
        guess = input(f"That was not {secret_length} letters! Try again: ")
    if (len(guess)) == secret_length and guess != secret_word:  # this final statement is for when you have the correct legth but the wrong word 
        while ind < len(secret_word):
            if (guess[ind] == secret_word[ind]):  # this if statement prints a green box if the letters are the same 
                emoji_result = emoji_result + GREEN_BOX
            else: 
                somewhere_else: bool = False  # keeps track if the guessed character exists elsewhere
                alt_indices: int = 0  # tracks the alternate indices and moves letter my letter each pass of the loop
                while somewhere_else is False and alt_indices < secret_length:  # this while loop uses the new variables and checks if there are other existing letters 
                    if (secret_word[alt_indices] == guess[ind]):
                        somewhere_else = True  # if there are letters, it changes is it true 
                    else: 
                        alt_indices = alt_indices + 1
                    if (somewhere_else is True):  # if its true, meaning the letter is found elsewhere, it assigns the yellow box 
                        emoji_result = emoji_result + YELLOW_BOX
                    else:  # if it isnt found else where, it assigns the white box because the letter isnt in there 
                        emoji_result = emoji_result + WHITE_BOX
                ind = ind + 1
            print(emoji_result)  # all of the boxes are printed on a single line corresponding to each letter 
            print("Not quite. Play again soon!") 
            playing = False  # loop is exitied 