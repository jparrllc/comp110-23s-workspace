"""EX06 - Choose Your Own Adventure."""
__author__ = "730479825"

import random

# global variables
points: int = 0
player: str = ""

# constants
EYES_EMOJI = "\U0001F440"
MONEYBAG_EMOJI = "\U0001F4B0"
TADA_EMOJI = "\U0001F389"
BEER_EMOJI = "\U0001F37A"
HAPPY_EMOJI = "\U0001F600"
HURT_EMOJI = "\U0001F915"


def greet() -> None:
    """Greats the player and introduces the game."""
    global player
    print(f"Welcome to the Midevil times Adventure Game! {TADA_EMOJI} Your goal here brave knight is to collect as much coin as possible in the form of {MONEYBAG_EMOJI}!!! ")
    player = input("What's your name brave knight? ")


def treasure() -> None:
    """Player goes out in hunt of treasure and tries to add to his coin pile."""
    global points
    print(f" Sir {player}, you explore a nearby cave and find a hidden treasure {MONEYBAG_EMOJI}. Do you take it?")
    choice: str = input("Enter 'y' for yes or 'n' for no: ")
    if choice == "y":
        worth: int = random.randint(50, 100)
        points += worth
        print(f"The treasure was worth {worth} {MONEYBAG_EMOJI}!")
    else:
        print("You missed out on the treasure. Better luck next time!")


def tavern() -> int:
    """Player heads to a tavern where their drink cost changes at random."""
    global points
    print(f"Sir {player}, you head to a nearby tavern. Do you buy an ale? {BEER_EMOJI}")
    choice: str = input("Enter 'y' for yes or 'n' for no: ")
    if choice == "y":
        number_of_ales = int(input("How many ales would you like? "))
        cost: int = 20 * number_of_ales
        points -= cost
        print(f"You bought {number_of_ales} ale(s) for {cost} {MONEYBAG_EMOJI} total at 20 {MONEYBAG_EMOJI} per drink.")
        return points
    else:
        print("You decided not to drink. Maybe next time!")
        return 0


def forest() -> None:
    """Player heads into a forest and gets lost, they try to navigate out."""
    global points
    print(f"Sir {player}, you are lost in a forest. Which way do you go?")
    direction: str = input("Enter 'left', 'right', or 'straight': ")
    if direction == "left":
        points += 20
        print(f"You found a shortcut with a small chest and gained 20 {MONEYBAG_EMOJI}! {HAPPY_EMOJI}")
    elif direction == "right":
        points -= 10
        print(f"You took a wrong turn, got beat up by a gang of elves and lost 10 {MONEYBAG_EMOJI} {HURT_EMOJI}.")
    else:
        print("You walked a long way but found nothing.")


def main() -> None:
    """Main function that acts as the guide to the players adventure and calls upon other functions."""
    greet()
    play_game = True
    while play_game:
        print(f"Coin Counter: {points} {MONEYBAG_EMOJI}")
        print("Where do you want to go next?")
        print("1. Find treasure")
        print("2. Relax at the tavern")
        print("3. Navigate a forest")
        print("4. End the game")
        choice = input("Enter 1, 2, 3, or 4: ")
        if choice == "1":
            treasure()
        elif choice == "2":
            tavern()
        elif choice == "3":
            forest()
        elif choice == "4":
            print(f"Goodbye, {player}! You accumulated {points} coins.")
            again: str = input("Do you want to play again? Enter 'y' for yes or 'n' for no: ")
            if again == "n":
                play_game = False
            

if __name__ == "__main__":
    main()