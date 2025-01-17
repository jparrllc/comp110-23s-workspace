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

print(emojified("yikyak","tiktok"))