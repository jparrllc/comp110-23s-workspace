"""EX03 - Structured Wordle"""
__author__ = "730479825"

def contains_char(string: str, character: str) ->bool:
    """Evaluates to check if the single character is found in the string"""
    assert len(character) == 1
    checking: bool = True  
    string_idx: int = 0
     
    while checking and string_idx < len(string):
        if string[string_idx] == character:
            checking = False 
            return True 
        else: 
            string_idx = string_idx + 1
    return False

def emojified(secret: str, guess: str) ->str:
    """Checks to see if letters in guess are found in the secret and gives emoji responses"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guess_idx: int = 0
    secret_idx: int = 0
    emojies: str = ""

    while guess_idx < len(guess):
        guess_let: str = ""
        secret_let: str = ""
        guess_let = guess[guess_idx]
        secret_let = secret[secret_idx]
        if guess_let == secret_let:
            emojies = emojies + GREEN_BOX 
            guess_idx = guess_idx + 1
            secret_idx = secret_idx + 1
        elif contains_char(guess, secret_let) == True:
            emojies = emojies + YELLOW_BOX
            guess_idx =  guess_idx + 1
            secret_idx = secret_idx + 1
        elif contains_char(guess, secret_let) == False:
            emojies = emojies + WHITE_BOX
            guess_idx = guess_idx + 1
            secret_idx = secret_idx + 1
    return emojies

def input_guess(expected_length: int) -> str:
    """Asks the user for a certain length guess, if it is the wrong length, it will continue to prompt them untill it is the correct length"""
    guess = input(f"Enter a {expected_length} character word: ") 
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    if len(guess) == expected_length:
        return guess
    return

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    correct_length: int = len(secret_word)
    turn_num: int = 1
    playing: bool = True 
    guess: str = ""

    while turn_num < 7 and playing:
        print(f"=== Turn {turn_num}/6 ===")
        guess = input_guess(correct_length)
        print (emojified(guess,secret_word))
        if guess == secret_word:
            playing = False
            print(f"You won in {turn_num}/6 turns!")
        turn_num = turn_num + 1
    if turn_num == 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()   