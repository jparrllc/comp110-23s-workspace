"""EX03 - Structured Wordle"""
__author__ = "730479825"

def contains_char(string: str, character: str) ->bool:  # function used to check if a single character is found within a string 
    """Evaluates to check if the single character is found in the string"""
    assert len(character) == 1  # forces the length of the character to be 1
    checking: bool = True  
    string_idx: int = 0
     
    while checking and string_idx < len(string):  # checking acts as a on/off switch for the while loop
        if string[string_idx] == character:  # if the character is in the string the loop stops and "true" is returned to denote that it is in the string
            checking = False 
            return True 
        else:  # if they are not equal it moves to the next character
            string_idx = string_idx + 1
    return False  # once it has gone through every character, and nothing matches, "false" is returned

def emojified(secret: str, guess: str) ->str:  # function that uses the previous function and assigns colored emojies
    """Checks to see if letters in guess are found in the secret and gives emoji responses"""
    assert len(guess) == len(secret)  # forces the length of the guess to be the length of the secret
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guess_idx: int = 0  # used to index the guess
    secret_idx: int = 0  # used to index the secret
    emojies: str = ""  # empty string that will be filled with colored boxes

    while guess_idx < len(guess):  # while loop that runs through the length of the guess and compares it to the secret. If letters align, green box, if they are found elsewhere, yellow, if not found, white.
        guess_let: str = "" # denotes guess and used for equality
        secret_let: str = "" # denotes secret and used for contains_char
        guess_let = guess[guess_idx]
        secret_let = secret[secret_idx]
        if guess_let == secret_let:  # if statement that puts a greenbox of they are the same
            emojies = emojies + GREEN_BOX 
            guess_idx = guess_idx + 1  # moves up one index
            secret_idx = secret_idx + 1  # moves up one index
        elif contains_char(guess, secret_let) == False:  # else if statment that prescribes a white box if said index letter is not found in secret, implementation of contains_char to see if letter is in word
            emojies = emojies + WHITE_BOX
            guess_idx = guess_idx + 1  # moves up one index
            secret_idx = secret_idx + 1  # moves up one index
        elif contains_char(guess, secret_let) == True: # else if statment that prescribes a yellow box if said index letter is not found in secret, implementation of contains_char to see if letter is in word
            emojies = emojies + YELLOW_BOX
            guess_idx =  guess_idx + 1  # moves up one index
            secret_idx = secret_idx + 1  # moves up one index
    return emojies  # returns the full string of colored boxes

def input_guess(expected_length: int) -> str:  # function that checcks if user input is the correct length of a prompted length input 
    """Asks the user for a certain length guess, if it is the wrong length, it will continue to prompt them untill it is the correct length"""
    guess = input(f"Enter a {expected_length} character word: ")  # input for a word of prompted length
    while len(guess) != expected_length:  # while the user inputs words of the wrong length the program asks over and over
        guess = input(f"That wasn't {expected_length} chars! Try again: ")  # the ask to reinput the correct length word 
    if len(guess) == expected_length:  # if it is the correct length, it returns the word input
        guess = guess
    return guess  # return request for the word

def main() -> None:  # main wordle function. woop woop!
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    correct_length: int = len(secret_word)  # sets desired length to length of secret word
    turn_num: int = 1  # used to denote what turn you are on
    playing: bool = True 
    guess: str = ""  # user input of guessed word 

    while turn_num < 7 and playing:  # playing acts as an on/off switch
        print(f"=== Turn {turn_num}/6 ===")  # displays what tuen you are on
        guess = input_guess(correct_length)  # insured user guess is right length using input_guess
        print (emojified(guess,secret_word))  # uses emojified to see what letters coincide with the secret word 
        if guess == secret_word: # if statement denoting what to do if the user guesses correctly 
            playing = False
            print(f"You won in {turn_num}/6 turns!")  # print out of how many turns it took
        turn_num = turn_num + 1  # moves to next turn
    if turn_num == 7:  # user only gets 6 turns to get it right, once they complete the 6th turn th game ends 
        print("X/6 - Sorry, try again tomorrow!")  # printed out when game ends

if __name__ == "__main__":
    main()   