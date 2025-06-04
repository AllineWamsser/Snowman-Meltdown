"""
    Core game logic für Snowman Meltdown
    
    """

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Selects a random word from the list.

        Rerturns: A randomly selected word.

    """

    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the current game state, including ASCII art and word progress

    args:
    mistake(int): Number of incorrent guesses
    secret_word (str): The secret word to guess
    guessed_letters (list): list of letters guessed so far

    """
    print(STAGES[mistakes])

    display = ""
    for letter in secret_word:
        display += f"{letter}" if letter in guessed_letters else "_ "

    print("Word:", display.strip())
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("Guessed letters:", " ".join(guessed_letters))


def play_game():
    """
    Main gameplay loop. Handles guessing logic and win/lose conditions

    """

    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes,secret_word,guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You´ve  already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes,secret_word,guessed_letters)
            print("Congratulations! You saved the snowman! ⛄")
            return

    display_game_state(mistakes,secret_word,guessed_letters)
    print(f"The snowman melted!💧The word was: {secret_word}")


if __name__ == "__main__":
    play_game()